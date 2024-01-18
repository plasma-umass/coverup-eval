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

    for file in coverup_output.iterdir():
        log = file / "coverup-log"
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
                            yield file, llm_utils.calculate_cost(last_usage['prompt_tokens'], last_usage['completion_tokens'], MODEL)
                        last_usage = usage

            if last_usage:
                yield file, llm_utils.calculate_cost(last_usage['prompt_tokens'], last_usage['completion_tokens'], MODEL)

def get_events():
    coverup_output = Path("output")

    for file in coverup_output.iterdir():
        log = file / "coverup-log"
        if log.exists():
            log_content = log.read_text()
            for m in re.finditer('---- (?:(\S+) )?(\S+):(\d+)-(\d+) ----\n\n?(.*)\n', log_content):
                timestamp, py, begin, end, first_line = m.groups()

                if first_line.startswith("The code below,"): # prompt
                    yield 'P', file, py, int(begin), int(end)
                elif first_line.startswith("Executing the test yields an error"):
                    yield 'F', file, py, int(begin), int(end)
                elif first_line.startswith("Executing the test along with"): # side effect
                    yield 'F', file, py, int(begin), int(end)
#                elif first_line.startswith("```python"): # response
#                    pass
                elif first_line.startswith("This test still lacks coverage"):
                    yield 'U', file, py, int(begin), int(end)
                elif first_line.startswith("Saved as"): # success
                    yield 'G', file, py, int(begin), int(end)


#def get_loc():
#    replication = codamosa / "replication"
#    modules_csv = replication / "test-apps" / "good_modules.csv"
#
#    loc = defaultdict(int)
#
#    with modules_csv.open() as f:
#        reader = csv.reader(f)
#        for d, m in reader:
#            base_module = m.split('.')[0]
#            file = replication / d / (m.replace('.','/') + ".py")
#            with file.open("rb") as mf:
#                loc[base_module] += sum(1 for _ in mf)
#
#    return loc

def get_modules():
    replication = codamosa / "replication"
    base = replication / "test-apps"

    with (base / "good_modules.csv").open() as f:
        reader = csv.reader(f)
        for d, m in reader:
            base_module = m.split('.')[0]
            path_to_src = replication / d
            rel_path = path_to_src.relative_to(base)
            src_dir = Path(*rel_path.parts[1:])     # rel_path.parts[0] is package name
            py = src_dir / (m.replace('.','/') + ".py")
            yield py, base_module

py2base = dict()
for py, base_module in get_modules():
    py2base[str(py)] = base_module

cost = defaultdict(int)

for file, usage in get_usage():
    cost[file] += usage

loc = defaultdict(int)
events = defaultdict(lambda: defaultdict(int))

for ev, file, py, begin, end in get_events():
    base_module = py2base[py]
    if ev == 'P':
        loc[base_module] += end-begin
    events[base_module][ev] += 1


headers=["Directory", "$", "LOC prompted", "$/1k LOC", "P", "G", "F", "U"]

def table():
    total=0
    for file in sorted(cost.keys(), key=lambda f:cost[f], reverse=True):
        base_module = file.name
        if '.' in base_module: base_module = base_module.split('.')[0]
        yield str(file), round(cost[file], 2), loc[base_module], round(cost[file]/loc[base_module]*1000, 2), \
              events[base_module]['P'], events[base_module]['G'], events[base_module]['F'], events[base_module]['U']
        total += cost[file]

    yield 'total', round(total, 2), *([None] * (len(headers)-2))

print(tabulate(table(), headers=headers))

