#
# FIXME FIXME This script is out of date!!
# 
from pathlib import Path
import ast
import re
import llm_utils
import csv
from collections import defaultdict
from tabulate import tabulate

MODEL='gpt-4-1106-preview'
codamosa = Path("codamosa")

def get_usage():
    coverup_output = Path("output")

    for out_dir in coverup_output.iterdir():
        log = out_dir / "coverup-log"
        last_usage = None
        if log.exists():
            log_content = log.read_text()
            no_startup = re.match('^---- (?:(\S+) )?startup ----\n', log_content) is None
            last_command = None
            for m in re.finditer('---- (?:(\S+) )?(\S+) ----\n\n?(.+(?:\n[^-].*)?)\n', log_content):
                timestamp, seg, first_lines = m.groups()
                if seg == 'startup':
                    if m:= re.search('^Command: (.*)$', first_lines, re.MULTILINE):
                        # This version uses checkpoints, so multiple starts may be restarts of the same work. 
                        # Detect a new run when different options are passed (in particular, a different coverage file).
                        if last_usage and last_command and m.group(1) != last_command:
#                            print(out_dir, last_usage)
                            yield out_dir, llm_utils.calculate_cost(last_usage['prompt_tokens'], last_usage['completion_tokens'], MODEL)
                            last_usage = None

                        last_command = m.group(1)

                if m := re.match('^total usage: (.*)', first_lines):
                    usage = ast.literal_eval(m.group(1))
                    if no_startup and last_usage and usage['prompt_tokens'] < last_usage['prompt_tokens']:
                        # this version didn't use checkpoints, so a lower prompt_tokens means it is another run
#                        print(out_dir, last_usage)
                        yield out_dir, llm_utils.calculate_cost(last_usage['prompt_tokens'], last_usage['completion_tokens'], MODEL)

                    last_usage = usage

            if last_usage:
#                print(out_dir, last_usage)
                yield out_dir, llm_utils.calculate_cost(last_usage['prompt_tokens'], last_usage['completion_tokens'], MODEL)

def get_events():
    coverup_output = Path("output")

    for out_dir in coverup_output.iterdir():
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
#                    pass
                elif first_line.startswith("This test still lacks coverage"):
                    yield 'U', out_dir, py, int(begin), int(end)
                elif first_line.startswith("Saved as"): # success
                    yield 'G', out_dir, py, int(begin), int(end)

cost = defaultdict(int)

for out_dir, usage in get_usage():
    cost[out_dir] += usage

loc = defaultdict(int)
events = defaultdict(lambda: defaultdict(int))

for ev, out_dir, py, begin, end in get_events():
    events[out_dir][ev] += 1
    if ev == 'P':
        loc[out_dir] += end-begin


headers=["Directory", "$", "LOC prompted", "$/1k LOC", "P", "G", "F", "S", "U"]

def table():
    total=0
    for out_dir in sorted(cost.keys(), key=lambda f:cost[f], reverse=True):
        base_module = out_dir.name
        if '.' in base_module: base_module = base_module.split('.')[0]
        yield str(out_dir), round(cost[out_dir], 2), loc[out_dir], round(cost[out_dir]/loc[out_dir]*1000, 2), \
              *[events[out_dir][k] for k in "PGFSU"]
        total += cost[out_dir]

    yield 'total', round(total, 2), *([None] * (len(headers)-2))

print(tabulate(table(), headers=headers))

