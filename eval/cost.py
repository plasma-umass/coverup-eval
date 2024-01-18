from pathlib import Path
import ast
import re
import llm_utils
import csv
from collections import defaultdict
from tabulate import tabulate

MODEL='gpt-4-1106-preview'
codamosa = Path("/home/juan") / "codamosa" # FIXME

def get_usage():
    coverup_output = Path("output")

    for out_dir in coverup_output.iterdir():
        log = out_dir / "coverup-log"
        last_usage = None
        if log.exists():
            with log.open("r") as f:
                for line in f.readlines():
                    m = re.match('^total usage: (.*)$', line, re.MULTILINE)
                    if m:
                        usage = ast.literal_eval(m.group(1))
                        # CoverUp may be started multiple times; look for restarts by when prompt_tokens drops
                        # and return maximum from each run
                        if last_usage and usage['prompt_tokens'] < last_usage['prompt_tokens']:
                            yield out_dir, llm_utils.calculate_cost(last_usage['prompt_tokens'], last_usage['completion_tokens'], MODEL)
                        last_usage = usage

            if last_usage:
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
                    yield 'F', out_dir, py, int(begin), int(end)
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


headers=["Directory", "$", "LOC prompted", "$/1k LOC", "P", "G", "F", "U"]

def table():
    total=0
    for out_dir in sorted(cost.keys(), key=lambda f:cost[f], reverse=True):
        base_module = out_dir.name
        if '.' in base_module: base_module = base_module.split('.')[0]
        yield str(out_dir), round(cost[out_dir], 2), loc[out_dir], round(cost[out_dir]/loc[out_dir]*1000, 2), \
              events[out_dir]['P'], events[out_dir]['G'], events[out_dir]['F'], events[out_dir]['U']
        total += cost[out_dir]

    yield 'total', round(total, 2), *([None] * (len(headers)-2))

print(tabulate(table(), headers=headers))

