from pathlib import Path
from collections import defaultdict
import json
import re
import csv
from statistics import mean, median

replication = Path("codamosa") / "replication"  # 'codamosa' links to its replication package
coverup_output = Path("output")

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--modules', choices=['good', '1_0'], default='good',
                    help='set of modules to compare')

    ap.add_argument('--config', type=str, help='specify a (non-default) configuration to use')

    ap.add_argument('--codamosa-results', choices=['gpt4', 'codex'], default='gpt4',
                    help='codamosa results to use')

    ap.add_argument('--plot', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot results instead of showing a table')

    ap.add_argument('--histogram', choices=['coverage', 'delta', 'lines', 'lines+branches'],
                    help='draw a histogram')

    ap.add_argument('--coverup-name', default='CoverUp', help="set CoverUp's name")

    return ap.parse_args()

args = parse_args()

modules_csv = replication / "test-apps" / f"{args.modules}_modules.csv"
coverup_output = coverup_output / (args.modules + (f".{args.config}" if args.config else ""))
codamosa_output = replication / f"output-{args.codamosa_results}"

modules_list = []
with modules_csv.open() as f:
    reader = csv.reader(f)
    for d, m in reader:
        dp = Path(d)
        assert dp.parts[0] == 'test-apps'

        modules_list.append({
            'name': m,
            'base_module': m.split('.')[0],
            'source_dir': str(Path(*dp.parts[2:])) + "/" if len(dp.parts) > 2 else ''
        })

by_module = defaultdict(dict)
coverup_totals = defaultdict(int)
codamosa_totals = defaultdict(int)
def add_to_totals(totals, module, summ):
    totals['count'] += 1
    line_keys = ['covered_lines', 'missing_lines']
    branch_keys = ['covered_branches', 'missing_branches']
    for k in line_keys + branch_keys:
        totals[k] += summ[k]

    lines = summ['covered_lines'] + summ['missing_lines']
    branches = summ['covered_branches'] + summ['missing_branches']

    if module in by_module:
        if by_module[module]['lines'] != lines:
            print(f"*** lines differ for {module}: {by_module[module]['lines']} vs {lines}")
        if by_module[module]['branches'] != branches:
            print(f"*** branches differ for {module}: {by_module[module]['branches']} vs {branches}")

    by_module[module]['lines'] = lines
    by_module[module]['branches'] = branches


codamosa = defaultdict(list)
coverup = dict()
codamosa_metrics = defaultdict(lambda: {'lines': [], 'branches': [], 'lines+branches': []})
coverup_metrics = defaultdict(dict)

def cover_pct(summ, cov_types, context):
    nom = sum(summ[f"covered_{c}"] for c in cov_types)
    den = nom + sum(summ[f"missing_{c}"] for c in cov_types)
    return 100*nom/den if den > 0 else None

if args.modules == '1_0':
    for m in modules_list:
        codamosa[m['name']] = [100.0]
        codamosa_metrics[m['name']]['lines'] = [100.0]
        codamosa_metrics[m['name']]['branches'] = [100.0]
        codamosa_metrics[m['name']]['lines+branches'] = [100.0]

else:
    assert args.modules == 'good'
    for f in codamosa_output.iterdir():
        m = re.match('(.*?)-\d+', f.name)
        module = m.group(1)
        file = module.replace('.','/') + ".py"

        with f.open() as jsonf:
            try:
                cov = json.load(jsonf)
            except json.decoder.JSONDecodeError as e:
                print(f"*** Error reading {str(f)}: {e}")
                continue

        assert file in cov['files']
        if file in cov['files']:
            summ = cov['files'][file]['summary']
            codamosa[module].append(summ['percent_covered'])
            add_to_totals(codamosa_totals, module, summ)

            pct = cover_pct(summ, ['lines'], f.name)
            if pct is not None: codamosa_metrics[module]['lines'].append(pct)
            pct = cover_pct(summ, ['branches'], f.name)
            if pct is not None: codamosa_metrics[module]['branches'].append(pct)
            pct = cover_pct(summ, ['lines','branches'], f.name)
            if pct is not None: codamosa_metrics[module]['lines+branches'].append(pct)


for m in modules_list:
    m_name = m['name']
    base_module = m['base_module']

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

    file = m['source_dir'] + m_name.replace('.','/') + ".py"
    assert file in cov['files']
    if file in cov['files']:
        summ = cov['files'][file]['summary']
        coverup[m_name] = summ['percent_covered']
        add_to_totals(coverup_totals, m_name, summ)

        pct = cover_pct(summ, ['lines'], m_name)
        if pct is not None: coverup_metrics[m_name]['lines'] = pct
        pct = cover_pct(summ, ['branches'], m_name)
        if pct is not None: coverup_metrics[m_name]['branches'] = pct
        pct = cover_pct(summ, ['lines','branches'], m_name)
        if pct is not None: coverup_metrics[m_name]['lines+branches'] = pct

module_names = sorted(codamosa.keys()|coverup.keys())
cov_codamosa = [mean(codamosa[m]) if codamosa[m] else None for m in module_names]
cov_coverup = [coverup[m] if m in coverup else None for m in module_names]
cov_delta = [cu - cm for cu, cm in zip(cov_coverup, cov_codamosa) if cu is not None and cm is not None]

cov_codamosa_l = [mean(codamosa_metrics[m]['lines']) for m in module_names if codamosa_metrics[m]['lines']]
cov_codamosa_b = [mean(codamosa_metrics[m]['branches']) for m in module_names if codamosa_metrics[m]['branches']]
cov_coverup_l = [coverup_metrics[m]['lines'] for m in module_names if 'lines' in coverup_metrics[m]]
cov_coverup_b = [coverup_metrics[m]['branches'] for m in module_names if 'branches' in coverup_metrics[m]]


if args.plot or args.histogram:
    import matplotlib.pyplot as plt
    import numpy as np

    plt.rcParams.update({
        'font.weight': 'bold',
        'pdf.fonttype': 42  # output TrueType; bigger but scalable
    })

    codamosa_label = f"CodaMosa ({args.codamosa_results})"

    if args.histogram:
        fig, ax = plt.subplots()
        ax.set_ylabel('Frequency', size=18)

        fig.set_size_inches(16, 8)

        if args.histogram == 'coverage':
            ax.set_title('Combined (translucent) Lines+Branches Coverage Histogram', size=20)
            ax.set_xlabel('% Coverage', size=18)

            bins = 40
            ax.hist(cov_coverup, bins=bins, alpha=.5, label=args.coverup_name, color='blue')
            ax.hist(cov_codamosa, bins=bins, alpha=.5, label=codamosa_label, color='yellow')

            ax.legend(loc='upper left', fontsize=15)

            fig.tight_layout()

        elif args.histogram == 'delta':
            ax.set_title('Delta Coverage Histogram', size=20)
            ax.set_xlabel(f'({args.coverup_name} - {codamosa_label}) % Coverage', size=18)
            ax.hist(cov_delta, bins=40)

        elif args.histogram == 'lines':
            ax.set_title('Lines per Module Histogram', size=20)
            ax.set_xlabel('# Lines in Module', size=18)
            ax.hist([by_module[m]['lines'] for m in module_names], bins=100)

        elif args.histogram == 'lines+branches':
            ax.set_title('Lines+Branches per Module Histogram', size=20)
            ax.set_xlabel('# Lines + # Branches in Module', size=18)
            ax.hist([by_module[m]['lines']+by_module[m]['branches'] for m in module_names], bins=100)

        fig.savefig('histogram.pdf')
    else:
        fig, ax = plt.subplots()
        ax.set_title(f'Coverage increase {args.coverup_name} vs. {codamosa_label} (larger is better)', size=20)
        ax.set_ylabel('% coverage increase', size=18)

        colors = ['green' if d>0 else 'black' for d in cov_delta]
        bars_x = np.arange(len(cov_delta))

        ax.bar(bars_x, cov_delta, .7, color=colors)
        ax.set_xticks([])

        fig.set_size_inches(16, 8)
        fig.tight_layout()

        fig.savefig('plot.pdf')

else:
    from tabulate import tabulate

    headers=["Module", "Lines", "Branches", "CoverUp %", "CodaMosa %", "samples"]
    def table():
        from simple_colors import red, green

        for m, cu, cm in zip(module_names, cov_coverup, cov_codamosa):
            if cm is not None:
                cm = round(cm, 2)

            if cm is not None and cu is not None:
                if cu >= cm:
                    cu = green(f"{cu:5.2f}")
                else:
                    cu = red(f"{cu:5.2f}")

            yield m, by_module[m]['lines'], by_module[m]['branches'], cu, cm, len(codamosa[m])

    print(tabulate(table(), headers=headers))

    def pct_cover(source, counters):
        nom = sum(source[f"covered_{c}"] for c in counters)
        den = nom + sum(source[f"missing_{c}"] for c in counters)
        return (f"{100*nom/den:.1f}%  " if den>0 else "") +\
               f"({nom}/{den})"

    cov_coverup = [c for c in cov_coverup if c is not None]
    cov_codamosa = [c for c in cov_codamosa if c is not None]

    print("")
    print(f"coverup l:             {len(cov_coverup_l):3} benchmarks, {mean(cov_coverup_l):.1f}% mean, " +\
          f"{median(cov_coverup_l):.1f}% median, {min(cov_coverup_l):.1f}% min, {max(cov_coverup_l):.1f}% max, " +\
          f"{sum(c==100 for c in cov_coverup_l)} @ 100%")
    print(f"coverup b:             {len(cov_coverup_b):3} benchmarks, {mean(cov_coverup_l):.1f}% mean, " +\
          f"{median(cov_coverup_b):.1f}% median, {min(cov_coverup_l):.1f}% min, {max(cov_coverup_l):.1f}% max, " +\
          f"{sum(c==100 for c in cov_coverup_b)} @ 100%")
    print(f"coverup l+b:           {len(cov_coverup):3} benchmarks, {mean(cov_coverup):.1f}% mean, " +\
          f"{median(cov_coverup):.1f}% median, {min(cov_coverup):.1f}% min, {max(cov_coverup):.1f}% max, " +\
          f"{sum(c==100 for c in cov_coverup)} @ 100%")
    print(f"   overall line cov.:     {pct_cover(coverup_totals, ['lines'])}")
    print(f"   overall branch cov.:   {pct_cover(coverup_totals, ['branches'])}")
    print(f"   overall l+b cov.:      {pct_cover(coverup_totals, ['lines','branches'])}")

    print("")
    codamosa_hdr = f"codamosa ({args.codamosa_results}) l:"
    print(f"{codamosa_hdr:22} {len(cov_codamosa_l):3} benchmarks, {mean(cov_codamosa_l):.1f}% mean, " +\
          f"{median(cov_codamosa_l):.1f}% median, {min(cov_codamosa_l):.1f}% min, {max(cov_codamosa_l):.1f}% max, " +\
          f"{sum(c==100 for c in cov_codamosa_l)} @ 100%")
    codamosa_hdr = f"codamosa ({args.codamosa_results}) b:"
    print(f"{codamosa_hdr:22} {len(cov_codamosa_b):3} benchmarks, {mean(cov_codamosa_b):.1f}% mean, " +\
          f"{median(cov_codamosa_b):.1f}% median, {min(cov_codamosa_b):.1f}% min, {max(cov_codamosa_b):.1f}% max, " +\
          f"{sum(c==100 for c in cov_codamosa_b)} @ 100%")
    codamosa_hdr = f"codamosa ({args.codamosa_results}) l+b:"
    print(f"{codamosa_hdr:22} {len(cov_codamosa):3} benchmarks, {mean(cov_codamosa):.1f}% mean, " +\
          f"{median(cov_codamosa):.1f}% median, {min(cov_codamosa):.1f}% min, {max(cov_codamosa):.1f}% max, " +\
          f"{sum(c==100 for c in cov_codamosa)} @ 100%")
    if codamosa_totals:
        print(f"   overall line cov.:     {pct_cover(codamosa_totals, ['lines'])}")
        print(f"   overall branch cov.:   {pct_cover(codamosa_totals, ['branches'])}")
        print(f"   overall l+b cov.:      {pct_cover(codamosa_totals, ['lines','branches'])}")

    better_count = sum([v > 0 for v in cov_delta])
    worse_count = sum([v < 0 for v in cov_delta])

    print('')
    print(f"improvement: +{better_count} ({100*better_count/len(cov_delta):.1f}%)/" +\
                       f"-{worse_count}/{len(cov_delta):3} benchmarks")
