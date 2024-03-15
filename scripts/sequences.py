from pathlib import Path
import re
from collections import defaultdict
from tabulate import tabulate

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--modules', choices=['good', '1_0'], default='good',
                    help='set of modules to compare')

    ap.add_argument('--show', type=str,
                    help='print out instances of a given sequence')

    ap.add_argument('--skip', type=str,
                    help='skip files containing this string')

    ap.add_argument('logs', type=str, help='log files to process')
    return ap.parse_args()

args = parse_args()


def get_events(log: Path):
    log_content = log.read_text()
#    for m in re.finditer('---- (?:(\S+) )?(\S+):(\d+)-(\d+) ----\n\n?(.*)\n', log_content):
    for m in re.finditer('---- (?:(\S+) )?([\S+ ]+) ----\n\n?(.*?)(?=\n---- |\Z)', log_content, re.DOTALL):
        timestamp, event, entry = m.groups()

        if event == 'startup':
            yield 'startup', timestamp, None
            continue

        if not (m := re.match('(\S+):(\d+)-(\d+)', event)):
            continue

        py, begin, end = m.groups()

        def what():
            if entry.startswith(("The code below,", "You are an expert")): # prompt
                if "\nwhen tested, it does not execute." in entry:
                    return 'P'
                return 'C'
            elif entry.startswith("Executing the test yields an error"):
                return 'F'
            elif entry.startswith("Executing the test along with"): # side effect
                return 'S'
            elif entry.startswith("```python"): # response
                return 'R'
            elif entry.startswith("This test still lacks coverage"):
                return 'U'

            elif entry.startswith("Saved as"): # success
                return 'G'
            elif entry.startswith("Missing modules"):
                return 'M'
            elif entry.startswith("measure_coverage timed out"):
                return 'T'
            elif entry.startswith("No Python code in GPT response"):
                return '-'
            elif entry.startswith("Too many attempts"): # gave up
                return '*'
            else:
                return '?'

        if what() in ('R', '?'): continue

        yield what(), timestamp, (py, int(begin), int(end))

seq_count = defaultdict(int)

def add_seqs(events):
    for k, v in events.items():
        if args.show and args.show == v:
            print(f"{k} {v}")

        # Only count sequences that reached a terminal state,
        # or else we would count partial executions (when
        # CoverUp gets interrrupted)
        if v[-1] in ('G', 'M', 'T', '-', '*'):
            seq_count[v] += 1

for file in (Path('output') / args.modules).glob(args.logs):
    if args.skip and args.skip in str(file):
        continue

    events = defaultdict(str)
    for ev, ts, details in get_events(file):
        if ev == 'startup':
            add_seqs(events)
            events = defaultdict(str)
            continue

        (py, begin, end) = details
        events[f"{py}:{begin}-{end}"] += ev

    add_seqs(events)

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
    if seq[0] == 'P': p_count[seq] += count
print('')
print(tabulate(mktable(p_count), headers=["seq", "count", "%"]))

c_count = defaultdict(int)
for seq, count in seq_count.items():
    if seq[0] == 'C': c_count[seq] += count
print('')
print(tabulate(mktable(c_count), headers=["seq", "count", "%"]))

# final states
end_count = defaultdict(int)
for seq, count in seq_count.items():
    end_count[seq[-1]] += count

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
