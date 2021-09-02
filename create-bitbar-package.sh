#!/bin/bash
#
# Copyright(C) 2018 Bitbar Technologies Oy
#
# NOTE: contributions are welcome
#
# __author__ = 'Niko Cankar <niko.cankar@bitbar.com>'


# Print how script is used and exit
function print_help_and_die() {
    echo "Usage: $0 <ios|android>"
    exit 0
}

if [[ "$#" -eq 1 ]]; then
    ENV="$1"
else
    print_help_and_die
fi

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

TEST_FILE="test-package_${ENV}.zip"

rm ${TEST_FILE}

echo "Creating test file for environment: ${ENV}"
cp run-tests_${ENV}.sh run-tests.sh && sed -i -e 's/\r$//' run-tests.sh && zip -r "${TEST_FILE}" tests/ pages/ requirements.txt  run-tests.sh
echo "
You should now upload test file '${TEST_FILE}' to Bitbar Cloud"