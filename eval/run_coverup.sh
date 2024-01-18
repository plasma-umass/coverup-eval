SRC=$1; shift
PKG=$1; shift
FILES=$@

OWNER=`stat -c %u /output`:`stat -c %g /output`

run() {
    echo $1
    eval $1 || exit 1
}

cd /output

# create writable version of the package
if ! [ -d package ]; then
    run "cp -R /package ."

    # requirementslib has a variable named _fragment_dict and pydantic, if also installed,
    # causes load failures (saying it should be renamed to fragment_dict).
    run "sed -i '/requirementslib/d' package/$SRC/package.txt"
    run "chown -R $OWNER /output"
fi

run "cd package"

run "pip install -r $SRC/package.txt || true"    # ignore any errors because so did CodaMOSA
run "pip install -r /coverup/requirements.txt -r /coverup/test-modules.txt"

PYTEST_ARGS="--rootdir . -c /dev/null" # ignore configuration which would deviate from expected defaults
SLIPCOVER_ARGS="--source $SRC/$PKG --branch --json"
COVERUP_ARGS="--write-requirements-to /output/requirements.txt --log-file /output/coverup-log --source-dir $SRC/$PKG --tests-dir coverup-tests --pytest-args \"$PYTEST_ARGS\""

[ -d coverup-tests ] || mkdir coverup-tests

# generate initial coverage file where nothing is covered
if ! [ -e /output/initial.json ]; then
    cat >coverup-tests/test_dummy.py <<XXX
def test_dummy():
    pass
XXX

    run "python3 -m slipcover $SLIPCOVER_ARGS --out /output/initial.json -m pytest $PYTEST_ARGS coverup-tests"
    rm coverup-tests/test_dummy.py

    run "chown -R $OWNER /output"
fi

# set Python path so the package can be 'import'ed
export PYTHONPATH=$SRC

# 1st pass
if ! [ -e /output/interim.json ]; then
    # run CoverUp on it
    run "python3 /coverup/coverup.py $COVERUP_ARGS --no-initial-test-check /output/initial.json $FILES"
    run "mv coverup-ckpt.json coverup-ckpt-0.json"

    # measure where coverage's at
    run "python3 -m slipcover $SLIPCOVER_ARGS --out /output/interim.json -m pytest $PYTEST_ARGS coverup-tests"

    run "chown -R $OWNER /output"
fi

# 2nd pass: re-run to try to improve coverage
if ! [ -e /output/final.json ]; then
    run "python3 /coverup/coverup.py $COVERUP_ARGS /output/interim.json $FILES"

    # measure final coverage
    run "python3 -m slipcover $SLIPCOVER_ARGS --out /output/final.json -m pytest $PYTEST_ARGS coverup-tests"

    run "chown -R $OWNER /output"
fi
