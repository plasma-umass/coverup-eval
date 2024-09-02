SLIPCOVER_ARGS=""
COVERUP_ARGS="--model gpt-4o-2024-05-13 --max-attempts 3 --isolate-tests --prompt-family gpt-v2 --install-missing-modules --write-requirements-to missing-modules.txt"
PYTEST_FINAL_ARGS=" --cleanslate"

if [ $PKG == "mimesis" ]; then
    # tests are randomized, so prone to flakies
    COVERUP_ARGS+=" --repeat-tests 20"
else
    COVERUP_ARGS+=" --repeat-tests 5"
fi
