#!/bin/bash

SMOKE_TEST_ONE=/home/codamosa/smoke-test-results/exp-220608-1749/mosa
pushd $SMOKE_TEST_ONE > /dev/null

GOOD_MODULES=`echo $(awk -F, '{print $2}' ~/test-apps/good_modules.csv) | tr " " "|"`

# Using "Benchmarks which have 1 coverage at end", excluding those already in good_modules.csv
tail -n 1 */statistics.csv | awk -F, '{print $NF}' | grep -B 1 '"1\.0"'  | grep ==  | sed 's/ *==> \(.*\)-[01]\/.*/\1/g' | sort | uniq | egrep -v $GOOD_MODULES > /tmp/1_0_modules.txt

popd > /dev/null

rm -f ~/test-apps/1_0_modules.csv
while read module; do
        module_expr="${module//./\\.}"
        grep "$module_expr\$" ~/test-apps/all_potential_modules.csv >> ~/test-apps/1_0_modules.csv
done < /tmp/1_0_modules.txt
