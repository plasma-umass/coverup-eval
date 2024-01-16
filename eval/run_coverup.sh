SRC=$1; shift
PKG=$1; shift
FILES=$@

OWNER=`stat -c %u /output`:`stat -c %g /output`

run() {
    echo $1
    eval $1 || exit 1
}

run "cp -R /package ."
run "cd package"

# requirementslib has a variable named _fragment_dict and pydantic, if also installed,
# causes load failures (saying it should be renamed to fragment_dict).
run "sed -i '/requirementslib/d' package.txt"

run "pip install -r package.txt || true"    # ignore any errors because so did CodaMOSA
run "pip install -r /coverup/requirements.txt"
run "pip install -r /coverup/test-modules.txt"

PYTEST_ARGS="--rootdir . -c /dev/null" # ignore configuration which would deviate from expected defaults
SLIPCOVER_ARGS="--source $SRC/$PKG --branch --json"

# generate initial coverage file where nothing is covered
mkdir coverup-tests
cat >coverup-tests/test_dummy.py <<XXX
def test_dummy():
    pass
XXX
run "python3 -m slipcover $SLIPCOVER_ARGS --out /output/initial.json -m pytest $PYTEST_ARGS coverup-tests"
run "chown -R $OWNER /output"

# set Python path so the package can be 'import'ed
export PYTHONPATH=$SRC

# run CoverUp on it
COVERUP_ARGS="--no-checkpoint --write-requirements-to /output/requirements.txt --log-file /output/coverup-log --source-dir $SRC/$PKG --tests-dir coverup-tests --pytest-args \"$PYTEST_ARGS\""
run "python3 /coverup/coverup.py $COVERUP_ARGS /output/initial.json $FILES"
run "chown -R $OWNER /output"

# measure where coverage's at
run "rm coverup-tests/test_dummy.py"
run "python3 -m slipcover $SLIPCOVER_ARGS --out /output/interim.json -m pytest $PYTEST_ARGS coverup-tests"
run "chown -R $OWNER /output"

# re-run CoverUp to try to improve on it
echo "-------- 2nd run --------" >> /output/coverup-log
run "python3 /coverup/coverup.py $COVERUP_ARGS /output/interim.json $FILES"
run "cp -R coverup-tests /output"
run "chown -R $OWNER /output"

# measure final coverage
run "python3 -m slipcover $SLIPCOVER_ARGS --out /output/final.json -m pytest $PYTEST_ARGS coverup-tests"
run "chown -R $OWNER /output"
