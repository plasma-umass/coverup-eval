from pathlib import Path
from collections import defaultdict
import json
import re
import csv
from statistics import mean, median

replication = Path("codamosa") / "replication"  # 'codamosa' links to its replication package
coverup_output = Path("output")
codamosa_output = replication / "output"

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--modules', choices=['good', '1_0'], default='good',
                    help='set of modules to compare')

    ap.add_argument('--only-coverup', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='only show lines with CoverUp data')

    ap.add_argument('--plot', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot results instead of showing a table')

    ap.add_argument('--blue', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot "blue" bars indicating results without counterpart')

    ap.add_argument('--vlines', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot vertical lines showing difference, rather than bars')

    ap.add_argument('--abs', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot actual number of lines rather than percentage of code')

    return ap.parse_args()

args = parse_args()

modules_csv = replication / "test-apps" / f"{args.modules}_modules.csv"
coverup_output = coverup_output / args.modules

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

if args.modules == '1_0':
    for m in codamosa:
        codamosa[m] = [100.0]

else:
    assert args.modules == 'good'
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
    if cov_file.exists():
        with cov_file.open() as jsonf:
            cov = json.load(jsonf)
    else:
        cov = None
        ckpt_files = sorted((coverup_output / base_module).glob("coverup-ckpt-*.json"))
        if ckpt_files:
            with ckpt_files[-1].open() as jsonf:
                ckpt = json.load(jsonf)
            cov = ckpt.get('final_coverage')

        if not cov:
            continue

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

    fig, ax = plt.subplots()

    if args.vlines:
        ax.set_title('Percentual coverage achieved (larger is better)', size=20)

        cov_codamosa = []
        cov_coverup = []

        for m in sorted(codamosa.keys()):
            if m not in coverup:
                continue

            cm = mean(codamosa[m]) if codamosa[m] else None
            cu = coverup[m] if m in coverup else None

            if cm is not None and cu is not None:
                cov_codamosa.append(cm)
                cov_coverup.append(cu)

#        ax.plot(cov_codamosa, '.', label='CodaMosa')
#        ax.plot(cov_coverup, '.', label='CoverUp')
        for i, (cu, cm) in enumerate(zip(cov_coverup, cov_codamosa)):
            ax.vlines(x=i, ymin=min(cu, cm), ymax=max(cu, cm), color=('green' if cu>=cm else 'red'))
#            ax.plot([i, cu], [i, cu])

#        ax.legend(fontsize=15)
        ax.set_xticks([])

    else:
        ax.set_title('Coverage increase (larger is better)', size=20)
        if args.abs:
            ax.set_ylabel('coverage increase (lines+branches)', size=18)
        else:
            ax.set_ylabel('% coverage increase', size=18)

        cov_increase = []
        colors = []

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
                colors.append('green' if inc>0 else 'black')
            elif args.blue:
                if cu is not None:
                    cov_increase.append(cu)
                    colors.append('blue')
                elif cm is not None:
                    cov_increase.append(-cm)
                    colors.append('blue')

        bars_x = np.arange(len(cov_increase))
        ax.bar(bars_x, cov_increase, .7, color=colors)
        ax.set_xticks([])


    fig.set_size_inches(16, 8)
    fig.tight_layout()
    fig.savefig('plot.png')

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
            if cm is not None and cu is not None:
                if cu >= cm:
                    cu = green(f"{cu:5.2f}")
                else:
                    cu = red(f"{cu:5.2f}")
            yield m, l_b, cu, cm, len(codamosa[m])

    def print_totals():
        improvement = []
        cov_on_imp = []
        cov = []
        cod = []
        for m in codamosa:
            cm = round(mean(codamosa[m]),1) if codamosa[m] else None
            cu = round(coverup[m],1) if m in coverup else None

            if cm is not None and cu is not None:
                improvement.append(cu - cm)
                cov_on_imp.append(cu)

            if cu is not None:
                cov.append(cu)

            if cm is not None:
                cod.append(cm)

        print(f"{len(improvement)} benchmarks available for both")
        print(f"coverup:     {len(cov):3} benchmarks, {mean(cov):.2f}% mean, {median(cov):.2f}% median")
        print(f"codamosa:    {len(cod):3} benchmarks, {mean(cod):.2f}% mean, {median(cod):.2f}% median")
        better_count = sum([v > 0 for v in improvement])
        worse_count = sum([v < 0 for v in improvement])
        print(f"improvement: +{better_count} ({100*better_count/len(improvement):.1f}%)/-{worse_count}/{len(improvement):3} benchmarks, {mean(improvement):.2f}% mean, {median(improvement):.2f}% median;")
        print(f"             of these, coverup {mean(cov_on_imp):.2f}% mean, {median(cov_on_imp):.2f}% median")

    print(tabulate(table(), headers=headers))
    print_totals()
