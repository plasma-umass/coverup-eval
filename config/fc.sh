# Config file to use "find culprit" on previously generated test suites
# Assumes that all tests are named test_coverup_...py

source /eval/scripts/install-reqs.sh

run "/eval/scripts/reenable-disabled-tests coverup-tests"

if [ "$PKG" == "mimesis" ]; then
    run "pip install pytest-repeat"
    PYTEST_ARGS+=" --count 5"
fi

SLIPCOVER_ARGS+=" --source $SRC/$PKG --branch --json"
COVERUP_ARGS+=" --source-dir $SRC/$PKG --tests-dir coverup-tests --pytest-args \"$PYTEST_ARGS\""

run "coverup $COVERUP_ARGS --only --failing find-culprit --debug"
run "PYTHONPATH=$SRC python3 -m slipcover $SLIPCOVER_ARGS --out final.json -m pytest $PYTEST_ARGS --disable-warnings coverup-tests"
run "chown -R $OWNER /output"

exit 0
