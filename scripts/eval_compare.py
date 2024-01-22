from pathlib import Path
from collections import defaultdict
import json
import re
import csv
from statistics import mean

codamosa = Path("/home/juan") / "codamosa" # FIXME

replication = codamosa / "replication"
modules_csv = replication / "test-apps" / "good_modules.csv"
codamosa_output = replication / "output"
coverup_output = Path("output")

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--only-coverup', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='only show lines with CoverUp data')

    ap.add_argument('--plot', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot results instead of showing a table')

    ap.add_argument('--abs', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot actual number of lines rather than % of code')

    return ap.parse_args()

args = parse_args()
codamosa = defaultdict(list)
lines_and_branches = dict()
source_dir = dict()

with modules_csv.open() as f:
    reader = csv.reader(f)
    for d, m in reader:
        codamosa[m] # make sure it's in the dict
        base_module = m.split('.')[0]
        dp = Path(d)
        assert dp.parts[0] == 'test-apps'
        source_dir[m] = str(Path(*dp.parts[2:])) + "/" if len(dp.parts) > 2 else ''

for f in codamosa_output.iterdir():
    m = re.match('(.*?)-\d+', f.name)
    module = m.group(1)
    file = module.replace('.','/') + ".py"

    with f.open() as jsonf:
        cov = json.load(jsonf)

    if file in cov['files']:
        summ = cov['files'][file]['summary']
        codamosa[module].append(summ['percent_covered'])
        lines_and_branches[module] = summ['covered_lines']+summ['missing_lines'] +\
                                     summ['covered_branches']+summ['missing_branches']
    else:
        codamosa[module]

coverup = dict()

for m in codamosa:
    base_module = m.split('.')[0]

    cov_file = coverup_output / base_module / "final.json"
    if not cov_file.exists():
        continue

    with cov_file.open() as jsonf:
        cov = json.load(jsonf)

    file = source_dir[m] + m.replace('.','/') + ".py"
    if file in cov['files']:
        summ = cov['files'][file]['summary']
        coverup[m] = summ['percent_covered']
        lines_and_branches[m] = summ['covered_lines']+summ['missing_lines'] +\
                                summ['covered_branches']+summ['missing_branches']

from tabulate import tabulate

if args.plot:
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update({
        'font.weight': 'bold',
        'pdf.fonttype': 42  # output TrueType; bigger but scalable
    })

    cov_increase = []

    for m in sorted(codamosa.keys()):
        if m not in coverup:
            continue

        cm = mean(codamosa[m]) if codamosa[m] else None
        cu = coverup[m] if m in coverup else None

        if cm and cu:
            inc = cu - cm
            if args.abs:
                inc *= lines_and_branches[m] / 100

            cov_increase.append(inc)

    bars_x = np.arange(len(cov_increase))

    fig, ax = plt.subplots()
    ax.bar(bars_x, cov_increase, .7, color='black')
    ax.set_xticks([])

    ax.set_title('Coverage increase (larger is better)', size=18)
    if args.abs:
        ax.set_ylabel('coverage increase (lines+branches)')
    else:
        ax.set_ylabel('% coverage increase')

    fig.set_size_inches(16, 8)
    fig.tight_layout()
    fig.savefig('plot.jpg')

else:
    headers=["Module", "Lines+Branches", "CoverUp %", "CodaMosa %", "samples"]
    def table():
        from simple_colors import red, green

        for m in sorted(codamosa.keys()):
            if args.only_coverup and m not in coverup:
                continue

            cm = round(mean(codamosa[m]),1) if codamosa[m] else None
            cu = round(coverup[m],1) if m in coverup else None
            l_b = lines_and_branches[m] if m in lines_and_branches else None
            if cm and cu:
                if cu >= cm:
                    cu = green(f"{cu:5.2f}")
                else:
                    cu = red(f"{cu:5.2f}")
            yield m, l_b, cu, cm, len(codamosa[m])

    def count_improved():
        improved = 0
        improvement = 0
        total = 0 
        for m in codamosa:
            cm = round(mean(codamosa[m]),1) if codamosa[m] else None
            cu = round(coverup[m],1) if m in coverup else None
            if cm and cu:
                total += 1
                improvement += (cu - cm)
                if cu >= cm:
                    improved += 1

        return improvement/total, improved, total

    print(tabulate(table(), headers=headers))
    improvement, improved, total = count_improved()
    print(f"{improvement:.2f}% better;  {improved} improved ({improved/total*100:.1f}%)")
