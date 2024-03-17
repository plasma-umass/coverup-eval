#!/usr/bin/env bash

SRC=$1; shift
PKG=$1; shift
OPTS=$1; shift
FILES=$@
REPEAT=false

OWNER=`stat -c %u /output`:`stat -c %g /output`

run() {
    echo $1
    eval $1 || exit 1
}

run "cd /output"

if ! [ -e $SRC/$PKG ]; then
    run "mkdir -p $SRC"
    run "ln -s `realpath /package/$SRC/$PKG` $SRC"
fi

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

PYTEST_ARGS="--rootdir . -c /dev/null" # ignore configuration which would deviate from expected defaults

if $REPEAT; then
    run "pip install pytest-repeat"
    PYTEST_ARGS+=" --count 5"
fi

SLIPCOVER_ARGS="--source $SRC/$PKG --branch --json"
COVERUP_ARGS="--write-requirements-to requirements.txt --source-dir $SRC/$PKG --tests-dir coverup-tests --pytest-args \"$PYTEST_ARGS\" $OPTS"

[ -d coverup-tests ] || mkdir coverup-tests

# set Python path so the package can be 'import'ed
export PYTHONPATH=$SRC

# run coverup twice: once to get stated, then another to help fill any gaps
for RUN in 1 2 3; do
    if ! [ -e coverup-ckpt-$RUN.json ]; then
        # run CoverUp on it
        run "coverup $COVERUP_ARGS --log-file coverup-log-$RUN --checkpoint coverup-ckpt.json $FILES"
        run "chown -R $OWNER /output"
        run "mv coverup-ckpt.json coverup-ckpt-$RUN.json"
    fi
done

# measure final coverage
if ! [ -e /output/final.json ]; then
    run "python3 -m slipcover $SLIPCOVER_ARGS --out final.json -m pytest $PYTEST_ARGS coverup-tests"
    run "chown -R $OWNER /output"
fi
