#!/usr/bin/env bash

# FIXME DRY with run_coverup.sh

CONFIG=$1; shift
SRC=$1; shift
PKG=$1; shift
FILES=$@

OWNER=`stat -c %u /output`:`stat -c %g /output`

run() {
    echo $1
    eval $1 || exit 1
}

# load/run base settings (such as OpenAI key)
if [ -e /eval/config/common.sh ]; then
    source /eval/config/common.sh
fi

# load/run configuration-specific settings
if [ -e /eval/config/$CONFIG.sh ]; then
    source /eval/config/$CONFIG.sh
fi

run "cd /output"

# install CodaMOSA-computed package dependencies;
# requirementslib has a variable named _fragment_dict and pydantic, if also installed,
# causes load failures (saying it should be renamed to fragment_dict).
if ! [ -e package.txt ]; then
    run "cp /package/$SRC/package.txt ."
    run "sed -i '/requirementslib/d' package.txt"
fi
run "pip install -r package.txt || true"    # ignore any errors because so did CodaMOSA

# install CoverUp and common test modules
run "pip install /eval/coverup"
run "pip install -r /eval/coverup/test-modules.txt"

PYTEST_ARGS+=" --rootdir . -c /dev/null" # ignore configuration which would deviate from expected defaults
PYTEST_ARGS+=" --count 1" # running once is enough for coverage
SLIPCOVER_ARGS+=" --source $SRC/$PKG --branch --json"

[ -d coverage ] || mkdir coverage

# set Python path so the package can be 'import'ed
export PYTHONPATH=$SRC

shopt -s nullglob # allow empty expansion
for F in coverup-tests/test_coverup_*.py; do
    B=`basename $F .py`
    if ! [ -e coverage/$B.json ]; then
        run "python3 -m slipcover $SLIPCOVER_ARGS --out coverage/$B.json -m pytest -qq --disable-warnings $PYTEST_ARGS $PYTEST_FINAL_ARGS $F || [ \$? == 5 ]"
    fi
done
