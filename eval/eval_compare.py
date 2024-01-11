from pathlib import Path
from collections import defaultdict
import json
import re
from statistics import mean

codamosa = Path("/home/juan") / "codamosa" # FIXME

replication = codamosa / "replication"
codamosa_output = replication / "output"
coverup_output = Path("output")

codamosa = defaultdict(list)

for f in codamosa_output.iterdir():
    m = re.match('(.*?)-\d+', f.name)
    module = m.group(1)
    file = module.replace('.','/') + ".py"

    with f.open() as jsonf:
        cov = json.load(jsonf)

    if file in cov['files']:
        codamosa[module].append(cov['files'][file]['summary']['percent_covered'])
    else:
        codamosa[module] # make sure module is in the dict

coverup = dict()

for m in codamosa:
    base_module = m.split('.')[0]

    cov_file = coverup_output / base_module / "final.json"
    if not cov_file.exists():
        continue

    with cov_file.open() as jsonf:
        cov = json.load(jsonf)

    file = m.replace('.','/') + ".py"
    if file in cov['files']:
        coverup[m] = cov['files'][file]['summary']['percent_covered']

from tabulate import tabulate

headers=["Module", "CoverUp %", "CodaMOSA %", "samples"]
def table():
    from simple_colors import red, green

    for m in sorted(codamosa.keys()):
        cm = round(mean(codamosa[m]),1) if codamosa[m] else None
        cu = round(coverup[m],1) if m in coverup else None
        if cm and cu:
            if cu >= cm:
                cu = green(f"{cu:5.2f}")
            else:
                cu = red(f"{cu:5.2f}")
        yield m, cu, cm, len(codamosa[m])

print(tabulate(table(), headers=headers))
