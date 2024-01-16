import csv
from pathlib import Path
from collections import defaultdict
import subprocess
import os

codamosa = Path("/home/juan") / "codamosa"  # FIXME

replication = codamosa / "replication"
modules_csv = replication / "test-apps" / "good_modules.csv"

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('module', type=str, nargs='?',
                    help='only process the given module')

    ap.add_argument('--dry-run', default=False,
                    action=argparse.BooleanOptionalAction,
                    help=f'only print out the command(s), but don\'t execute them')

    ap.add_argument('--one', default=False,
                    action=argparse.BooleanOptionalAction,
                    help=f'just run one package and stop')

    return ap.parse_args()

args = parse_args()

pkg = defaultdict(list)

with modules_csv.open() as f:
    reader = csv.reader(f)
    for d, m in reader:
        pkg[d].append(m)

for d in pkg:
    if args.module and args.module not in d:
        continue

    package = pkg[d][0].split('.')[0]

    assert Path(d).parts[0] == 'test-apps'
    pkg_top = replication / Path(*Path(d).parts[:2]) # just 'test-apps' and top level
    src = (replication / Path(d)).relative_to(pkg_top)

    files = [str(src / (m.replace('.','/') + ".py")) for m in pkg[d]]

    output = Path("output") / package

    if output.exists() and not args.dry_run:
        continue

    if not args.dry_run:
        output.mkdir(parents=True)

    cmd = f"docker run --rm " +\
          f"-e OPENAI_API_KEY=\"{os.environ['OPENAI_API_KEY']}\" " +\
           "-v .:/coverup:ro " +\
          f"-v {str(output.absolute())}:/output " +\
          f"-v {str(pkg_top.absolute())}:/package:ro " +\
           "-t slipcover-runner " +\
          f"bash /coverup/eval/run_coverup.sh {src} {package} {' '.join(files)}"

    print(cmd)
    if not args.dry_run:
        subprocess.run(cmd, shell=True, check=True)

    if args.one:
        break
