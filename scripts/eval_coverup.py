import csv
from pathlib import Path
from collections import defaultdict
import subprocess
import os

test_apps = Path("codamosa/replication/test-apps")
pip_cache = Path("pip-cache")  # set to None to disable

def parse_args():
    import argparse
    ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    ap.add_argument('module', type=str, nargs='?',
                    help='only process the given module')

    ap.add_argument('--dry-run', default=False,
                    action=argparse.BooleanOptionalAction,
                    help=f'only print out the command(s), but don\'t execute them')

    ap.add_argument('--modules', choices=['good', '1_0'], default='good',
                    help='set of modules to process')

    ap.add_argument('--variant', type=str, help='specify an execution variant')

    ap.add_argument('--ablate', default=False, action='store_true')

    ap.add_argument('-i', '--interactive', default=False,
                    action=argparse.BooleanOptionalAction,
                    help=f'start interactive docker (rather than run CoverUp)')

    args = ap.parse_args()
    if args.ablate and not args.variant:
        args.variant = 'ablated'

    return args

args = parse_args()

modules_csv = test_apps / f"{args.modules}_modules.csv"

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
    pkg_top = test_apps / Path(d).parts[1] # just top level
    src = (test_apps / Path(*Path(d).parts[1:])).relative_to(pkg_top)

    files = [str(src / (m.replace('.','/') + ".py")) for m in pkg[d]]

    output = Path("output") / (args.modules + (f".{args.variant}" if args.variant else "")) / package

    if (output / "final.json").exists() and not (args.dry_run or args.interactive):
        continue

    if not args.dry_run:
        output.mkdir(parents=True, exist_ok=True)

    options="--ablate" if args.ablate else ""

    cmd = f"docker run --rm " +\
          f"-e OPENAI_API_KEY=\"{os.environ['OPENAI_API_KEY']}\" " +\
           "-v .:/eval:ro " +\
          f"-v {str(output.absolute())}:/output " +\
          f"-v {str(pkg_top.absolute())}:/package:ro " +\
           "-v ./pip-cache:/root/.cache/pip " +\
          ("-ti " if args.interactive else "-t ") +\
           "coverup-runner bash " +\
          (f"/eval/scripts/run_coverup.sh {src} {package} \"{options}\" {' '.join(files)}" if not args.interactive else "")

    print(cmd)
    if not args.dry_run:
        subprocess.run(cmd, shell=True, check=True)
