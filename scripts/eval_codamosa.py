import csv
from pathlib import Path
from collections import defaultdict
import subprocess

modules_csv = Path("test-apps") / "good_modules.csv"
codamosa_tests = Path("/home/juan/codamosa-dataset/final-exp/codamosa-0.8-uninterp")
output = Path("output-codamosa")

pkg = defaultdict(list)

with modules_csv.open() as f:
    reader = csv.reader(f)
    for d, m in reader:
        pkg[d].append(m)

output.mkdir(exist_ok=True)

for p in pkg:
    sample_module = pkg[p][0]
    if any([sample_module in str(f) for f in output.iterdir()]):
        continue # skip if already done

    pname = sample_module.split('.')[0]
#    if pname == 'sty': continue # dependency failure
#    if pname == 'isort': continue # all tests fail
#    if pname == 'py_backwards': continue # tests timeout using 100% CPU
#    if pname == 'tornado': continue # dependencies fail

    cmd =  "docker run --rm " +\
           "-v ./run_coda_tests.sh:/run_coda_tests.sh:ro " +\
          f"-v {str(codamosa_tests.absolute())}:/tests:ro " +\
          f"-v {str(output.absolute())}:/output " +\
          f"-v ./{p}:/package:ro " +\
           "-t slipcover-runner " +\
          f"bash /run_coda_tests.sh {' '.join(pkg[p])}"
    print(cmd)
    subprocess.run(cmd, shell=True, check=True)
