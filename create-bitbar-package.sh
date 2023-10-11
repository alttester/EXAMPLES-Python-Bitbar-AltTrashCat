#!/bin/bash
#
# Copyright(C) 2018 Bitbar Technologies Oy
#
# NOTE: contributions are welcome
#
# __author__ = 'Niko Cankar <niko.cankar@bitbar.com>'

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

TEST_FILE="test-package.zip"

rm ${TEST_FILE}

echo "Creating test file for environment iOS"
sed -i -e 's/\r$//' run-tests.sh && zip -r "${TEST_FILE}" tests/ pages/ requirements.txt  run-tests.sh
echo "
You should now upload test file '${TEST_FILE}' to Bitbar Cloud"