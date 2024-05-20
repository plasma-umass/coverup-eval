# Starting from a copy of the original results, compute the
# coverage obtained running tests in isolation.
#
# Preparatory steps:
#    cp -a output/good output/good.isolated
#    find output/good.isolated -name final.json -exec rm {} +
#
# Then:
#    python3 scripts/eval_coverup.py --config isolated

cd /output
run "/eval/scripts/reenable-disabled-tests coverup-tests"

COVERUP_ARGS+=" --isolate-tests"
PYTEST_ARGS+=" --cleanslate"
