from pathlib import Path
from collections import defaultdict
import json
import re
import csv
from statistics import mean, median
import sys

coverup_output = Path("output")
replication = Path("codamosa") / "replication"

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('--suite', choices=['good', '1_0'], default='good',
                    help='suite of modules to compare')

    ap.add_argument('--config', type=str, help='specify a (non-default) configuration to use for the first CoverUp')

    def other_system(value):
        coda_choices = [f'codamosa-{r}' for r in ['codex', 'codex-isolated', 'gpt4', 'gpt4-isolated', 'gpt4o']]
        if not (value.startswith('coverup-') or value in coda_choices):
            raise argparse.ArgumentTypeError(f'invalid choice: select {", ".join(coda_choices)} or coverup-..config..')
        return value

    ap.add_argument('--compare-to', '--to', type=other_system, default='codamosa-gpt4',
                    help='select what to compare to')

    ap.add_argument('--plot', default=False,
                    action=argparse.BooleanOptionalAction,
                    help='plot results instead of showing a table')

    ap.add_argument('--histogram', choices=['coverage', 'delta', 'lines', 'lines+branches'],
                    help='draw a histogram')

    ap.add_argument('--title', type=str, help='specify different title for --plot')

    ap.add_argument('--out', type=Path, help='specify alternative output file for --plot')

    return ap.parse_args()

args = parse_args()

def load_suite(suite_name):
    modules_list = []
    with (replication / "test-apps" / f"{suite_name}_modules.csv").open() as f:
        reader = csv.reader(f)
        for d, m in reader:
            dp = Path(d)
            assert dp.parts[0] == 'test-apps'

            modules_list.append({
                'name': m,
                'base_module': m.split('.')[0],
                'source_dir': str(Path(*dp.parts[2:])) + "/" if len(dp.parts) > 2 else ''
            })

    return {
        "name": suite_name,
        "modules": modules_list
    }


json_load_cache = dict()
def json_load(path):
    if path not in json_load_cache:
        with path.open() as f:
            json_load_cache[path] = json.load(f)

    return json_load_cache[path]


def load_coverup(suite, config = None):
    # per-module dictonary -> list of [coverage 'summary']
    data = defaultdict(list)

    config_output_dir = coverup_output / (suite['name'] + (f".{config}" if config else ""))

    if not config_output_dir.exists():
        print(f"Cannot load data: directory {config_output_dir} missing")
        sys.exit(1)

    for m in suite['modules']:
        m_name = m['name']
        m_out_dir = config_output_dir / m['base_module']

        cov_file = m_out_dir / "final.json"
        if cov_file.exists():
            cov = json_load(cov_file)
        else:
            cov = None
            ckpt_files = sorted(m_out_dir.glob("coverup-ckpt-*.json"))
            if ckpt_files:
                if ckpt_files[-1] not in json_load_cache: print(f"Note: using {ckpt_files[-1]}")

                ckpt = json_load(ckpt_files[-1])
                cov = ckpt.get('final_coverage')

            if not cov:
                continue

        file = m['source_dir'] + m_name.replace('.','/') + ".py"
        if file not in cov['files']:
            file = "/package/" + file
        assert file in cov['files'], f"{file} missing for {m_out_dir}"
        data[m_name].append(cov['files'][file]['summary'])

    return {
        "name": "CoverUp" + (f" ({config})" if config else ""),
        "data": data
    }


def load_codamosa(suite, coda_config):
    assert suite['name'] == 'good'

    config_output_dir = replication / f"output-{coda_config}"

    if not config_output_dir.exists():
        print(f"Cannot load data: directory {config_output_dir} missing")
        sys.exit(1)

    # list of per-file summaries
    data = defaultdict(list)

    for f in config_output_dir.iterdir():
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

    return {
        "name": f"CodaMosa ({coda_config})",
        "data": data
    }


def fake_full_coverage(loaded_dataset, name):
    # fake 100% coverage
    fake_data = defaultdict(list)

    for m in loaded_dataset:
        summ = loaded_dataset[m][0]
        fake_data[m].append({
            'covered_lines': summ['covered_lines'] + summ['missing_lines'],
            'covered_branches': summ['covered_branches'] + summ['missing_branches'],
            'missing_lines': 0,
            'missing_branches': 0
        })

    return {
        "name": name,
        "data": fake_data,
        "is_fake": True
    }


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


if __name__ == "__main__":
    suite = load_suite(args.suite)
    datasets = [load_coverup(suite, args.config)]

    second_config = args.compare_to[args.compare_to.index('-')+1:]
    if args.compare_to.startswith('codamosa-'):
        if args.suite == '1_0':
            datasets.append(fake_full_coverage(datasets[0]['data'], "CodaMosa (fake)"))
        else:
            datasets.append(load_codamosa(suite, second_config))
    else:
        datasets.append(load_coverup(suite, second_config))

#    module_names = sorted(datasets[0]['data'].keys() | datasets[1]['data'].keys())
    module_names = sorted(datasets[0]['data'].keys() & datasets[1]['data'].keys())

    # compute lines+branches coverage for easy access
    coverage_lb = []
    for ds in datasets:
        coverage_lb.append([mean_of(cover_pct(sample, ['lines','branches']) for sample in ds['data'][m]) for m in module_names])

    # compute delta between the two coverage_lb
    cov_delta = [a - b for a, b in zip(coverage_lb[0], coverage_lb[1]) if a is not None and b is not None]


    # compute lines and branches for each module, for easy access
    module_info = defaultdict(dict)
    for module, summ in datasets[0]['data'].items():
        summ = summ[0] # use 1st sample
        module_info[module]['lines'] = summ['covered_lines'] + summ['missing_lines']
        module_info[module]['branches'] = summ['covered_branches'] + summ['missing_branches']

    # show missing modules
    for i in range(len(datasets)):
        missing = set(mod['name'] for mod in suite['modules']) - set(datasets[i]['data'].keys())
        if missing:
            print(f"Missing in {datasets[i]['name']}: {', '.join(sorted(missing))}")
            print()

    if args.plot or args.histogram:
        import matplotlib.pyplot as plt
        import numpy as np

        plt.rcParams.update({
            'font.weight': 'bold',
            'pdf.fonttype': 42  # output TrueType; bigger but scalable
        })

        codamosa_label = datasets[1]['name']

        if args.histogram:
            fig, ax = plt.subplots()
            ax.set_ylabel('Frequency', size=18)

            fig.set_size_inches(16, 8)

            if args.histogram == 'coverage':
                ax.set_title('Combined (translucent) Lines+Branches Coverage Histogram', size=20)
                ax.set_xlabel('% Coverage', size=18)

                bins = 40
                ax.hist(coverage_lb[0], bins=bins, alpha=.5, label=datasets[0]['name'], color='blue')
                ax.hist(coverage_lb[1], bins=bins, alpha=.5, label=datasets[1]['name'], color='yellow')

                ax.legend(loc='upper left', fontsize=15)

                fig.tight_layout()

            elif args.histogram == 'delta':
                ax.set_title('Delta Coverage Histogram', size=20)
                ax.set_xlabel(f'({datasets[0]["name"]} - {datasets[1]["name"]}) % Coverage', size=18)
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
            if args.title:
                ax.set_title(args.title, size=20)
            else:
                ax.set_title(f'Coverage increase {datasets[0]["name"]} vs. {datasets[1]["name"]} (larger is better)', size=20)

            ax.set_ylabel('% coverage increase', size=18)

            colors = ['green' if d>0 else 'black' for d in cov_delta]
            bars_x = np.arange(len(cov_delta))

            ax.bar(bars_x, cov_delta, .7, color=colors)
            ax.set_xticks([])

            fig.set_size_inches(16, 8)
            fig.tight_layout()

            if args.out:
                fig.savefig(args.out)
            else:
                fig.savefig('plot.pdf')

    else:
        from tabulate import tabulate

        headers=["Module", "Lines", "Branches", datasets[0]['name'] + " %", datasets[1]['name'] + " %", "samples"]
        def table():
            from simple_colors import red, green

            for m, a, b in zip(module_names, coverage_lb[0], coverage_lb[1]):
                if a is not None: a = round(a, 2)
                if b is not None: b = round(b, 2)

                if a is not None and b is not None:
                    v = f"{a:5.2f}"
                    if a > b:
                        a = green(v)
                    elif a < b:
                        a = red(v)
                    else:
                        a = v

                yield m, module_info[m]['lines'], module_info[m]['branches'], a, b, len(datasets[1]['data'][m])

        print('')
        print(tabulate(table(), headers=headers))


        for ds in datasets:
            name = ds['name']
            dataset = ds['data']

            if 'is_fake' in ds and ds['is_fake']:
                continue

            print("")
            for metrics in [['lines'], ['branches'], ['lines','branches']]:
                label = '+'.join(metrics)
                short_label = '+'.join(m[0] for m in metrics)

                data = [mean_of(cover_pct(sample, metrics) for sample in dataset[m]) for m in dataset]
                data = [d for d in data if d is not None]

                print(f"{name + ' ' + short_label + ':':30} {len(data):3} benchmarks, {mean(data):.1f}% mean, " +\
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
        print(f"{datasets[0]['name']} did better on {better_count} ({100*better_count/len(cov_delta):.1f}%) " +\
                           f"and worse on {worse_count} benchmarks out of {len(cov_delta)}.")
