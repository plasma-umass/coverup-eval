from pathlib import Path
import ast
import re
import llm_utils
import csv
from collections import defaultdict
from tabulate import tabulate
import sys

def get_events():
    coverup_output = Path("output")

    for out_dir in coverup_output.iterdir():
        if '.' in out_dir.name: continue    # ignore things like "ansible.backup"
        log = out_dir / "coverup-log"
        if log.exists():
            log_content = log.read_text()
            for m in re.finditer('---- (?:(\S+) )?(\S+):(\d+)-(\d+) ----\n\n?(.*)\n', log_content):
                timestamp, py, begin, end, first_line = m.groups()

                if first_line.startswith("The code below,"): # prompt
                    yield 'P', out_dir, py, int(begin), int(end)
                elif first_line.startswith("Executing the test yields an error"):
                    yield 'F', out_dir, py, int(begin), int(end)
                elif first_line.startswith("Executing the test along with"): # side effect
                    yield 'S', out_dir, py, int(begin), int(end)
#                elif first_line.startswith("```python"): # response
#                    yield 'R', out_dir, py, int(begin), int(end)
                elif first_line.startswith("This test still lacks coverage"):
                    yield 'U', out_dir, py, int(begin), int(end)
                elif first_line.startswith("Saved as"): # success
                    yield 'G', out_dir, py, int(begin), int(end)
                elif first_line.startswith("Too many attempts"): # gave up
                    yield '*', out_dir, py, int(begin), int(end)

events = defaultdict(str)
for ev, out_dir, py, begin, end in get_events():
    key = f"{py}:{begin}-{end}"
    if key == "flutils/packages.py:53-87":
        print(ev, out_dir, py, begin, end)

    if "G" not in events[key]:
        events[key] += ev

#for key in events:
#    if events[key] == 'PPPG':
#        print(key)

seq_count = defaultdict(int)
for v in events.values():
    seq_count[v] += 1

def table():
    for seq, count in sorted(seq_count.items(), key=lambda item: item[1], reverse=True):
        yield seq, count

headers=["seq", "count"]
print(tabulate(table(), headers=headers))

