PYTEST_ARGS=""
SLIPCOVER_ARGS=""
COVERUP_ARGS="--isolate-tests"
PYTEST_FINAL_ARGS=" --cleanslate"

if [ $PKG == "mimesis" ]; then
    # tests are randomized, so prone to flakies
    COVERUP_ARGS+=" --repeat-tests 10"
fi
