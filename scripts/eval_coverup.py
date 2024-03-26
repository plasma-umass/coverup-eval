import csv
from pathlib import Path
from collections import defaultdict
import subprocess
import os

test_apps = Path("codamosa/replication/test-apps")
pip_cache = Path("pip-cache")  # set to None to disable
eval_path = Path(__file__).parent.parent

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

    ap.add_argument('--config', type=str, help='specify a (non-default) configuration to use')

    ap.add_argument('-i', '--interactive', default=False,
                    action=argparse.BooleanOptionalAction,
                    help=f'start interactive docker (rather than run CoverUp)')

    ap.add_argument('--pip-cache', default=True,
                    action=argparse.BooleanOptionalAction,
                    help=f'whether to pass in the pip cache')

    args = ap.parse_args()

    if args.interactive and not args.module:
        ap.error("module is required when using --interactive.")

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

    output = Path("output") / (args.modules + (f".{args.config}" if args.config else "")) / package

    if (output / "final.json").exists() and not (args.dry_run or args.interactive):
        continue

    if not args.dry_run:
        output.mkdir(parents=True, exist_ok=True)

    config = args.config if args.config else 'default'

    cmd = f"docker run --rm " +\
          f"-v {str(eval_path.absolute())}:/eval:ro " +\
          f"-v {str(output.absolute())}:/output " +\
          f"-v {str(pkg_top.absolute())}:/package:ro " +\
          (f"-v {str((eval_path / 'pip-cache').absolute())}:/root/.cache/pip " if args.pip_cache else "") +\
          ("-ti " if args.interactive else "-t ") +\
           "coverup-runner bash " +\
          (f"/eval/scripts/run_coverup.sh {config} {src} {package} {' '.join(files)}" if not args.interactive else "")

    print(cmd)
    if not args.dry_run:
        subprocess.run(cmd, shell=True, check=True)
