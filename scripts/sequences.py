from pathlib import Path
import re
from collections import defaultdict

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--suite', choices=['good', '1_0'], default='good',
                    help='suite of modules to compare')

    ap.add_argument('--config', type=str, help='specify a (non-default) configuration to use')

    ap.add_argument('--show', type=str,
                    help='print out instances of a given sequence')

    ap.add_argument('--check-c-p', action="store_true",
                    help='check for C prompts that are equivalent to a C prompt')

    ap.add_argument('--skip', type=str,
                    help='skip files containing this string')

    ap.add_argument('logs', type=str, help='log files to process')
    return ap.parse_args()


TERMINAL_EVENTS=('G', 'M', 'T', '-', '*')


def is_same_as_P(content, begin, end):
    """This attempts to detect 'C' (context) prompts that were only issued as context prompts
       because their 'def' executed when their module was loaded to 'P' (initial) prompts,
       which is what they should have been."""

    begin, end = int(begin), int(end)

    if (rng := re.search(r'^when tested, lines (\d+)-(\d+) do not execute', content, re.M)) and \
       (py := re.search('```python\n(.*)```', content, re.S)):
        first, last = int(rng.group(1)), int(rng.group(2))

        def del_line_markup(s):
            # CoverUp "   nnn: " line markup
            line_markup_len = 12
            s = '\n'.join(l[line_markup_len:] for l in s.splitlines())

            import textwrap
            return textwrap.dedent(s)

        try:
            import ast
            tree = ast.parse(del_line_markup(py.group(1)))
            block = next(iter(node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))), None)
            if block is None:
                block = next(iter(node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)))
        except Exception:
            print("----")
            print(py.group(1))
            print("----")
            print(del_line_markup(py.group(1)))
            print("----")
            raise

        if ast.get_docstring(block, clean=False) is not None:
            block.body.pop(0)

        for first_stmt in block.body:
            if not isinstance(first_stmt, (ast.Global, ast.Nonlocal)):
                break

        last_stmt = block.body[-1]

        block.lineno = min([block.lineno, *(d.lineno for d in block.decorator_list)])

        # CoverUp may include "class" statements in a segment, or it may start a segment
        # within the class and just emit "class" statements for context. We have no way
        # of knowing which one we're seeing, so we need to look for both cases (below).

        # We also need to allow the last line to fall anywhere within the last statement
        # because of things like:
        #     return (
        #         foo
        #     )

        if (begin - 1 + first_stmt.lineno == first and
              (begin - 1 + last_stmt.lineno <= last and
               begin - 1 + last_stmt.end_lineno >= last)):
            # segment started at line 1
            return True
        elif (begin - block.lineno + first_stmt.lineno == first and
            (begin - block.lineno + last_stmt.lineno <= last and
             begin - block.lineno + last_stmt.end_lineno >= last)):
            # segment started with the 'def', with other lines for context
            return True
#            else:
#                print("----")
#                print(f"{first=} {last=} {rng.group(0)=}")
#                print(f"{block.lineno=} {begin=}")
#                print(f"{first_stmt=} {begin - block.lineno + first_stmt.lineno} {first}")
#                print(f"{last_stmt=} {begin - block.lineno + last_stmt.end_lineno} {last}")
#                print(py.group(1))

    return False

def parse_log(log_content: str, check_c_p_equivalence=False):
    for m in re.finditer('---- (?:(\S+) )?([\S+ ]+) ----\n\n?(.*?)(?=\n---- |\Z)', log_content, re.DOTALL):
        timestamp, event, content = m.groups()

        if event == 'startup':
            yield timestamp, 'startup', None, content
            continue

        if not (m := re.match('(\S+):(\d+)-(\d+)', event)):
            continue

        py, begin, end = m.groups()

        def what():
            if content.startswith(("The code below,", "You are an expert")): # prompt
                if "\nwhen tested, it does not execute." in content:
                    return 'P'
                if check_c_p_equivalence and is_same_as_P(content, begin, end):
                    return 'p'
                return 'C'
            elif content.startswith("Executing the test yields an error"):
                return 'F'
            elif content.startswith("Executing the test along with"): # side effect
                return 'S'
            elif content.startswith("```python"): # response
                return 'R'
            elif content.startswith("This test still lacks coverage"):
                return 'U'
            elif content.startswith("Saved as"): # success
                return 'G'
            elif content.startswith("Missing modules"):
                return 'M'
            elif content.startswith("measure_coverage timed out"):
                return 'T'
            elif content.startswith("No Python code in GPT response"):
                return '-'
            elif content.startswith("Too many attempts"): # gave up
                return '*'
            else:
                return '?'

#        if what() == '?': print(content)

        yield timestamp, what(), (py, int(begin), int(end)), content


def get_sequences(log_content: str, check_c_p_equivalence=False):
    seqs = defaultdict(str)
    seq_ts = defaultdict(lambda:[])

    def yield_sequences():
        for seg, seq in seqs.items():
            # Only include sequences that reached a terminal
            # state, or else we'd count partial executions,
            # when CoverUp gets interrupted.
            if seq[-1] in TERMINAL_EVENTS:
                yield seg, seq, seq_ts[seg]
        seqs.clear()

    for ts, ev, details, _ in parse_log(log_content, check_c_p_equivalence):
        if ev == 'startup':
            yield from yield_sequences()
            continue

        (py, begin, end) = details

        if ev not in ('R', '?'):
            seg = f"{py}:{begin}-{end}"
            seqs[seg] += ev
            seq_ts[seg].append(ts)

    yield from yield_sequences()


if __name__ == '__main__':
    from tabulate import tabulate

    args = parse_args()

    seq_count = defaultdict(int)
    path = Path('output') / (args.suite + (f".{args.config}" if args.config else ""))
    for file in path.glob(args.logs):
        if '.' in file.name: # "foobar.failed" and such
            continue

        if args.skip and args.skip in str(file):
            continue

        for seg, seq, _ in get_sequences(file.read_text(), check_c_p_equivalence=args.check_c_p):
            if args.show and args.show == seq:
                print(f"{seg} {seq}")

            seq_count[seq] += 1


    def mktable(data):
        total = sum(data.values())
        for seq, count in sorted(data.items(), key=lambda item: item[1], reverse=True):
            yield seq, count, round(100*count/total, 1)

        yield '(total)', total, None

# all sequences
#    print(tabulate(mktable(seq_count), headers=["seq", "count", "%"]))

# P and C seqs
    for start in (('P','p'), ('C',)):
        p_count = defaultdict(int)
        for seq, count in seq_count.items():
            if seq[0] in start:
                seq = start[0] + seq[1:] # p -> P
                if seq[-1] in ('-', 'T', 'M'):
                    seq = seq[0] + '..' + seq[-1]
                p_count[seq] += count
        print('')
        print(tabulate(mktable(p_count), headers=["seq", "count", "%"]))

# final states
    end_count = defaultdict(int)
    for seq, count in seq_count.items():
        if seq[-1] == 'G':
            end_count[('.' * (len(seq)-1)) + 'G'] += count

    print('')
    print(tabulate(mktable(end_count), headers=["seq", "count", "%"]))

    end_count = defaultdict(int)
    for seq, count in seq_count.items():
        if seq[-1] == 'G':
            end_count[seq[0] + ('.' * (len(seq)-2)) + 'G'] += count

    print('')
    print(tabulate(mktable(end_count), headers=["seq", "count", "%"]))

    f_count = defaultdict(int)
    for seq, count in seq_count.items():
        if 'F' in seq:
            f_count['F'] += count
        elif seq[-1] == 'G':
            f_count['...G'] += count
        else:
            f_count[seq] += count

    print('')
    print(tabulate(mktable(f_count), headers=["seq", "count", "%"]))

## coverage prompts
#    cov_count = defaultdict(int)
#    for seq, count in seq_count.items():
#        if seq[0] == 'C':
#            cov_count[seq] += count
#
#    print('')
#    print(tabulate(mktable(cov_count), headers=["seq", "count", "%"]))
#
## where 'U' was followed by success
#    pug_count = defaultdict(int)
#    for seq, count in seq_count.items():
#        if 'U' in seq and seq[-1] == 'G':
#            pug_count[seq] += count
#
#    print('')
#    print(tabulate(mktable(pug_count), headers=["seq", "count", "%"]))
#
## where 'U' was followed by failure
#    pux_count = defaultdict(int)
#    for seq, count in seq_count.items():
#        if 'U' in seq and seq[-1] != 'G':
#            pux_count[seq] += count
#
#    print('')
#    print(tabulate(mktable(pux_count), headers=["seq", "count", "%"]))
