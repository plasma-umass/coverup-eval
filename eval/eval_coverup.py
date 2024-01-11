import csv
from pathlib import Path
from collections import defaultdict
import subprocess
import os

codamosa = Path("/home/juan") / "codamosa"  # FIXME

replication = codamosa / "replication"
modules_csv = replication / "test-apps" / "good_modules.csv"

pkg = defaultdict(list)

with modules_csv.open() as f:
    reader = csv.reader(f)
    for d, m in reader:
        pkg[d].append(m)

for d in pkg:
    package = pkg[d][0].split('.')[0]

    pkg_top = replication / Path(*Path(d).parts[:2]) # just 'test-apps' and top level
    src = (replication / Path(d)).relative_to(pkg_top)

    files = [str(src / (m.replace('.','/') + ".py")) for m in pkg[d]]

    output = Path("output") / package

    if output.exists():
        continue

    output.mkdir(parents=True)

#    cmd = f"docker run --user {os.getuid()}:{os.getgid()} --rm " +\
    cmd = f"docker run --rm " +\
          f"-e OPENAI_API_KEY=\"{os.environ['OPENAI_API_KEY']}\" " +\
           "-v .:/coverup:ro " +\
          f"-v {str(output.absolute())}:/output " +\
          f"-v {str(pkg_top.absolute())}:/package:ro " +\
           "-t slipcover-runner " +\
          f"bash /coverup/eval/run_coverup.sh {src} {package} {' '.join(files)}"
    print(cmd)
    subprocess.run(cmd, shell=True, check=True)
    break
