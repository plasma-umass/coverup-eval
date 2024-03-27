from pathlib import Path
from collections import defaultdict
import json
import re
import csv
from statistics import mean, median

coverup_output = Path("output")
replication = Path("codamosa") / "replication"

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

def load_modules_list(modules_csv: Path):
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

    return modules_list


def load_coverup(modules_list, config = None):
    # per-module dictonary -> list of [coverage 'summary']
    data = defaultdict(list)

    for m in modules_list:
        m_name = m['name']
        m_out_dir = coverup_output / (args.modules + (f".{config}" if config else "")) / m['base_module']

        cov_file = m_out_dir / "final.json"
        if cov_file.exists():
            with cov_file.open() as jsonf:
                cov = json.load(jsonf)
        else:
            cov = None
            ckpt_files = sorted(m_out_dir.glob("coverup-ckpt-*.json"))
            if ckpt_files:
                with ckpt_files[-1].open() as jsonf:
                    ckpt = json.load(jsonf)
                cov = ckpt.get('final_coverage')

            if not cov:
                continue

            print(f"Note: using {ckpt_files[-1]} for {m_name}")

        file = m['source_dir'] + m_name.replace('.','/') + ".py"
        assert file in cov['files']
        if file in cov['files']:
            data[m_name].append(cov['files'][file]['summary'])

    return data


def load_codamosa(codamosa_output):
    assert args.modules == 'good'

    # list of per-file summaries
    data = defaultdict(list)

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
            data[module].append(cov['files'][file]['summary'])

    return data


modules_list = load_modules_list(replication / "test-apps" / f"{args.modules}_modules.csv")
coverup_data = load_coverup(modules_list, args.config)

codamosa_data = load_codamosa(replication / f"output-{args.codamosa_results}")


def cover_pct(summ, cov_types):
    """Computes the percentage of coverage.

       summ: JSON "summary" from coverage measurement
       cov_types: either ['lines'], ['branches'] or ['lines','branches']
       return: percentage, or None if the denominator is 0.
    """
    nom = sum(summ[f"covered_{c}"] for c in cov_types)
    den = nom + sum(summ[f"missing_{c}"] for c in cov_types)
    return 100*nom/den if den > 0 else None


def mean_of(values):
    """Returns the mean of a list of values, ignoring any that are None.
       Returns None if there are no values to take the mean of.

       This is useful because some statistics may not be possible, such
       such as branch coverage when a module has no branches
    """
    clean = [v for v in values if v is not None]
    return mean(clean) if clean else None


module_names = sorted(codamosa_data.keys()|coverup_data.keys())
cov_codamosa = [mean_of(cover_pct(sample, ['lines','branches']) for sample in codamosa_data[m]) for m in module_names]
cov_coverup = [mean_of(cover_pct(sample, ['lines','branches']) for sample in coverup_data[m]) for m in module_names]

cov_delta = [cu - cm for cu, cm in zip(cov_coverup, cov_codamosa) if cu is not None and cm is not None]


# compute lines and branches for each module, for easy access
module_info = defaultdict(dict)
for module in coverup_data:
    summ = coverup_data[module][0]
    module_info[module]['lines'] = summ['covered_lines'] + summ['missing_lines']
    module_info[module]['branches'] = summ['covered_branches'] + summ['missing_branches']


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
            ax.hist([module_info[m]['lines'] for m in module_names], bins=100)

        elif args.histogram == 'lines+branches':
            ax.set_title('Lines+Branches per Module Histogram', size=20)
            ax.set_xlabel('# Lines + # Branches in Module', size=18)
            ax.hist([module_info[m]['lines']+module_info[m]['branches'] for m in module_names], bins=100)

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

            yield m, module_info[m]['lines'], module_info[m]['branches'], cu, cm, len(codamosa_data[m])

    print(tabulate(table(), headers=headers))

    sets = [
        ['coverup', coverup_data],
        [f'codamosa ({args.codamosa_results})', codamosa_data]
    ]

    for name, dataset in sets:
        print("")
        for metrics in [['lines'], ['branches'], ['lines','branches']]:
            label = '+'.join(metrics)
            short_label = '+'.join(m[0] for m in metrics)

            data = [mean_of(cover_pct(sample, metrics) for sample in dataset[m]) for m in dataset]
            data = [d for d in data if d is not None]

            print(f"{name + ' ' + short_label + ':':22} {len(data):3} benchmarks, {mean(data):.1f}% mean, " +\
                  f"{median(data):.1f}% median, {min(data):.1f}% min, {max(data):.1f}% max, " +\
                  f"{sum(c==100 for c in data)} @ 100%")

        for metrics in [['lines'], ['branches'], ['lines','branches']]:
            short_label = '+'.join(m[0] for m in metrics)
            covered = sum(sample[f'covered_{metric}'] for metric in metrics for m in dataset for sample in dataset[m])
            total = covered + sum(sample[f'missing_{metric}'] for metric in metrics for m in dataset for sample in dataset[m])

            pct = f"{100*covered/total:.1f}%  " if total>0 else ""
            print(f"   overall {short_label+':':6} {pct}({covered}/{total})")

    better_count = sum([v > 0 for v in cov_delta])
    worse_count = sum([v < 0 for v in cov_delta])

    print('')
    print(f"improvement: +{better_count} ({100*better_count/len(cov_delta):.1f}%)/" +\
                       f"-{worse_count}/{len(cov_delta):3} benchmarks")
