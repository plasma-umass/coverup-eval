#!/bin/bash
docker run --rm -v `pwd`/test-apps:/home/codamosa/test-apps -v `pwd`:/cwd -it benchmarks-image  /bin/bash /cwd/gen_1_0_modules.sh
