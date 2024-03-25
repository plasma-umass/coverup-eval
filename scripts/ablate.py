from pathlib import Path
from collections import defaultdict
import subprocess
import csv

modules_csv = Path("codamosa/replication/test-apps") / f"good_modules.csv"

pkg2dir = defaultdict(list)
with modules_csv.open() as f:
    reader = csv.reader(f)
    for p, m in reader:
        p = Path(p)
        assert p.parts[0] == 'test-apps'
        topdir = p.parts[1]
        pkg = m.split('.')[0]
        pkg2dir[pkg] = topdir

for d in Path("output/good").glob("*"):
    if '.' in d.name: continue

    abl = Path("output/good.ablated/" + d.name)
    if abl.exists(): continue

    cmd = f"scripts/prepare-ablated {d.name}"
    print(cmd)
    subprocess.run(cmd, shell=True, check=True)

    cmd = f"python3 scripts/eval_coverup.py --config ablate {pkg2dir[d.name]}"
    print(cmd)
    subprocess.run(cmd, shell=True, check=True)
#    break
