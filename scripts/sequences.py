from pathlib import Path
import re
from collections import defaultdict
from tabulate import tabulate

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--modules', choices=['good', '1_0'], default='good',
                    help='set of modules to compare')

    ap.add_argument('--variant', type=str, help='specify an execution variant')

    ap.add_argument('--show', type=str,
                    help='print out instances of a given sequence')

    ap.add_argument('--skip', type=str,
                    help='skip files containing this string')

    ap.add_argument('logs', type=str, help='log files to process')
    return ap.parse_args()

args = parse_args()


TERMINAL_EVENTS=('G', 'M', 'T', '-', '*')

def parse_log(log_content: str):
    for m in re.finditer('---- (?:(\S+) )?([\S+ ]+) ----\n\n?(.*?)(?=\n---- |\Z)', log_content, re.DOTALL):
        timestamp, event, content = m.groups()

        if event == 'startup':
            yield timestamp, 'startup', None
            continue

        if not (m := re.match('(\S+):(\d+)-(\d+)', event)):
            continue

        py, begin, end = m.groups()

        def what():
            if content.startswith(("The code below,", "You are an expert")): # prompt
                if "\nwhen tested, it does not execute." in content:
                    return 'P'
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

        yield timestamp, what(), (py, int(begin), int(end))


def get_sequences(log_content: str):
    seqs = defaultdict(str)

    def yield_sequences():
        for seg, seq in seqs.items():
            # Only include sequences that reached a terminal
            # state, or else we'd count partial executions,
            # when CoverUp gets interrupted.
            if seq[-1] in TERMINAL_EVENTS:
                yield seg, seq
        seqs.clear()

    for ts, ev, details in parse_log(log_content):
        if ev == 'startup':
            yield from yield_sequences()
            continue

        (py, begin, end) = details

        if ev not in ('R', '?'):
            seqs[f"{py}:{begin}-{end}"] += ev

    yield from yield_sequences()


seq_count = defaultdict(int)
for file in (Path('output') / (args.modules + (f".{args.variant}" if args.variant else ""))).glob(args.logs):
    if args.skip and args.skip in str(file):
        continue

    for seg, seq in get_sequences(file.read_text()):
        if args.show and args.show == seq:
            print(f"{seg} {seq}")

        seq_count[seq] += 1

total_seq = sum(seq_count.values())


def mktable(data):
    row_total = 0
    for seq, count in sorted(data.items(), key=lambda item: item[1], reverse=True):
        row_total += count
        yield seq, count, round(100*count/total_seq, 2)

    yield '(total)', row_total, round(100*row_total/total_seq, 2)

# all sequences
#print(tabulate(mktable(seq_count), headers=["seq", "count", "%"]))

# P and C seqs
p_count = defaultdict(int)
for seq, count in seq_count.items():
    if seq[0] == 'P':
        if seq[-1] in ('-', 'T', 'M'):
            seq = seq[0] + '..' + seq[-1]
        p_count[seq] += count
print('')
print(tabulate(mktable(p_count), headers=["seq", "count", "%"]))

c_count = defaultdict(int)
for seq, count in seq_count.items():
    if seq[0] == 'C':
        if seq[-1] in ('-', 'T', 'M'):
            seq = seq[0] + '..' + seq[-1]
        c_count[seq] += count
print('')
print(tabulate(mktable(c_count), headers=["seq", "count", "%"]))

# final states
end_count = defaultdict(int)
for seq, count in seq_count.items():
    end_count[seq[0] + ".." + seq[-1]] += count

print('')
print(tabulate(mktable(end_count), headers=["seq", "count", "%"]))

# coverage prompts
cov_count = defaultdict(int)
for seq, count in seq_count.items():
    if seq[0] == 'C':
        cov_count[seq] += count

print('')
print(tabulate(mktable(cov_count), headers=["seq", "count", "%"]))

# where 'U' was followed by success
pug_count = defaultdict(int)
for seq, count in seq_count.items():
    if 'U' in seq and seq[-1] == 'G':
        pug_count[seq] += count

print('')
print(tabulate(mktable(pug_count), headers=["seq", "count", "%"]))

# where 'U' was followed by failure
pux_count = defaultdict(int)
for seq, count in seq_count.items():
    if 'U' in seq and seq[-1] != 'G':
        pux_count[seq] += count

print('')
print(tabulate(mktable(pux_count), headers=["seq", "count", "%"]))
