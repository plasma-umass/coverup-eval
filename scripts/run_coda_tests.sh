cp -R /package .
cd package

sed -i '/requirementslib/d' package.txt
#sed -i '/python_apt/d' package.txt  # package yanked, not currently available
#sed -i '/bzr_pqm/d' package.txt     # seems Python 2.x specific
#sed -i '/disco==/d' package.txt     # tqdm doesn't seem to need it, and causes conflicts
#sed -i 's/pymake==0.4.3/py-make==0.1.0/' package.txt  # pymake isn't a proper module; tqdm's setup.cfg says py-make
#sed -i '/py2exe/d' package.txt # requires Windows
#if grep -q kerberos package.txt; then
#    apt update
#    apt-get install -y gcc g++      # needed to build certain Python packages
#    apt-get install -y libkrb5-dev  # for 'krb5-config' command
#fi

#pip install -U pip || exit 1
pip install -r package.txt #|| exit 1

for MOD in $@; do
    for ATTEMPT in /tests/$MOD-*; do
        A=`basename $ATTEMPT`
        TEST_FILE="$ATTEMPT/test_"`echo $MOD | sed "s/\./_/g"`".py"
        SRC_FILE=`echo $MOD | sed "s/\./\//g"`".py"
        # -s needed by ansible tests that try to read from stdout while pytest is capturing it
        CMD="timeout 120 python3 -m slipcover --branch --json --out /output/$A.json -m pytest --rootdir . -c /dev/null -p no:cacheprovider $TEST_FILE || rm /output/$A.json"
        echo $CMD
        eval $CMD
    done
done
