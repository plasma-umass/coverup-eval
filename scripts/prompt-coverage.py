from pathlib import Path
from collections import defaultdict
from sequences import parse_log, TERMINAL_EVENTS
import json
import re


def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--suite', choices=['good', '1_0', 'mutap'], default='good',
                    help='suite of modules to compare')

    ap.add_argument('--config', type=str, help='specify a (non-default) configuration to use')

    ap.add_argument('--filter-unprompted', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='filter out coverage that we did not prompt')

    ap.add_argument('--filter-c', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='only consider C prompts after successful P prompts')
    return ap.parse_args()

def get_tests(log_content: str):
    seqs = defaultdict(str)
    seq_file = dict()

    def yield_tests():
        for seg, seq in list(seqs.items()):
            if seq[-1] == 'G': #in TERMINAL_EVENTS:
                yield seg, seq[0], seq_file.get(seg, None)
                del seqs[seg]
                if seg in seq_file:
                    del seq_file[seg]

    for ts, ev, details, content in parse_log(log_content, check_c_p_equivalence=True):
        if ev == 'startup':
            yield from yield_tests()
            continue

        (py, begin, end) = details

        if ev == 'p': ev = 'P'  # P-equivalent C prompt

        if ev not in ('R', '?'):
            seg = f"{py}:{begin}-{end}"
            seqs[seg] += ev
            if ev == 'G':
                m = re.match('Saved as (.*)', content)
                seq_file[seg] = m.group(1)

    yield from yield_tests()


def load_json(file: Path):
    with file.open("r") as f:
        return json.load(f)


def empty_cov(branch_coverage: bool) -> dict:
    import datetime

    return {
        'meta': {
            'software': 'slipcover',
            'version': slipcover.__version__,
            'timestamp': datetime.datetime.now().isoformat(),
            'branch_coverage': branch_coverage,
            'show_contexts': False
        },
        'files': dict()
    }

if __name__ == "__main__":
    import copy
    from slipcover import slipcover
    from eval_coverup import load_suite
    from tabulate import tabulate

    args = parse_args()
    suite = load_suite(args.suite)

    entries = []
    totals = {
        'start': defaultdict(int),
        'P': defaultdict(int),
        'C': defaultdict(int)
    }

    for pkg in sorted((Path('output') / (args.suite + (f".{args.config}" if args.config else ""))).glob('*')):
        if '.' in pkg.name: # "foobar.failed" and such
            continue

        cov = {
            'start': load_json(pkg / "coverup-ckpt-1.json")['coverage'],
            'P': empty_cov(branch_coverage=True),
            'C': empty_cov(branch_coverage=True)
        }

        def filter_cov(f_cov, valid_lines):
            return {
                'executed_lines': [l for l in f_cov['executed_lines'] if l in valid_lines],
                'missing_lines': [l for l in f_cov['missing_lines'] if l in valid_lines],
                'executed_branches': [b for b in f_cov['executed_branches'] if b[0] in valid_lines],
                'missing_branches': [b for b in f_cov['missing_branches'] if b[0] in valid_lines]
            }

        valid_P_lines = defaultdict(set)

        for logfile in sorted(pkg.glob('coverup-log-*')):
            for seg, prompt, test in get_tests(logfile.read_text()):
                file = seg.split(':')[0]
                line_range = tuple(map(int, (seg.split(':')[1]).split('-')))
                valid_lines = set(range(line_range[0], line_range[1]+1))

                if args.filter_c:
                    if prompt == 'P':
                        valid_P_lines[file].update(valid_lines)
                    elif prompt == 'C':
                        valid_lines = valid_lines.intersection(valid_P_lines[file])

#                print(seg, file, valid_lines, prompt, test)

                test = Path(test)
                if test.is_absolute() and test.parts[1] == 'output':
                    test = Path(*test.parts[2:])

                test_cov = load_json(pkg / "coverage" / (test.stem + ".json"))

                if args.filter_unprompted:
                    test_cov['files'] = {file: filter_cov(test_cov['files'][file], valid_lines)}

                slipcover.merge_coverage(cov[prompt], test_cov)


        final = load_json(pkg / "final.json")
        pkg_info = [suite[d] for d in suite if suite[d]['package'] == pkg.name][0]
        if pkg_info['files']:
            # limit only to files for which we requested coverage, not test files, etc.
            pkg_files = set(pkg_info['files'])
            for c in [*cov.values(), final]:
                c['files'] = {k:v for k,v in c['files'].items() if k in pkg_files}
                slipcover.add_summaries(c)

        def pct(cov):
            return round(cov['summary']['percent_covered'], 1)

        if not args.filter_unprompted:
            slipcover.merge_coverage(cov['P'], cov['start'])

        slipcover.merge_coverage(cov['C'], cov['P'])

        entries.append([
            pkg.name,
            cov['C']['summary']['covered_lines'] + cov['C']['summary']['missing_lines'],
            pct(cov['start']), 
            pct(cov['P']),
            pct(cov['C']),
            pct(cov['C']) - pct(cov['P'])
        ])

        entries = sorted(entries, key=lambda x: x[-1], reverse=True)

        for k in cov:
            for n in ['covered_lines', 'missing_lines', 'covered_branches', 'missing_branches']:
                totals[k][n] += cov[k]['summary'][n]

        if args.filter_c and args.filter_unprompted and cov['P']['summary']['percent_covered'] > cov['C']['summary']['percent_covered']:
            print(f"{pkg.name:20} start: {pct(cov['start'])} init.prompt: {pct(cov['P'])} cov.prompt: {pct(cov['C'])}")
            for f in cov['P']['files']:
                if f not in cov['C']['files']:
                    print(f"{f} missing from C")
                    continue

                if cov['P']['files'][f]['summary']['percent_covered'] > cov['C']['files'][f]['summary']['percent_covered']:
                    print(f"{f} goes down:")
                    print(f"    P: {cov['P']['files'][f]}")
                    print(f"    C: {cov['C']['files'][f]}")

        if not args.filter_unprompted and pct(cov['C']) != pct(final):
            print(f"{pkg.name:20} start: {pct(cov['start'])} init.prompt: {pct(cov['P'])} cov.prompt: {pct(cov['C'])}")
            for f in final['files']:
                if f not in cov['C']['files']:
                    print(f"{f} missing from C")
                    continue

                if cov['C']['files'][f]['summary'] != final['files'][f]['summary']:
                    print(f"{f} differs:")
                    print(f"    C: {cov['C']['files'][f]}")
                    print(f"    f: {final['files'][f]}")

    def calc_pct(cov, t):
        d = cov[f"covered_{t}"]+cov[f"missing_{t}"]
        if not d:
            return 0

        return round(100*cov[f"covered_{t}"]/d, 1)

    entries.append([])
    entries.append([
        'lines mean',
        totals['C']['covered_lines'] + totals['C']['missing_lines'],
        calc_pct(totals['start'], 'lines'),
        calc_pct(totals['P'], 'lines'),
        calc_pct(totals['C'], 'lines'),
        calc_pct(totals['C'], 'lines')-calc_pct(totals['P'], 'lines')
    ])
    entries.append([
        'branches mean',
        totals['C']['covered_branches'] + totals['C']['missing_branches'],
        calc_pct(totals['start'], 'branches'),
        calc_pct(totals['P'], 'branches'),
        calc_pct(totals['C'], 'branches'),
        calc_pct(totals['C'], 'branches')-calc_pct(totals['P'], 'branches')
    ])

    print(tabulate(entries, headers=[
        'package',
        'lines/br.',
        'start %',
        'after init. prompts %',
        'after cov. prompts %',
        'delta %',
    ]))
