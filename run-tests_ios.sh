#!/bin/bash

# Name of the test file
TEST=${TEST:="BitbarSampleAppTest.py"}

echo "Extracting tests.zip..."
unzip -o tests.zip

echo "Installing pip requirements"
chmod 0755 requirements.txt
apt-get --assume-yes install python3.7
python3 --version
python3.7 --version
python3.7 -m pip install --upgrade pip
python3.7 -m pip install wheel
python3.7 -m pip install -r requirements.txt
python3.7 -m pip list

#########################################################
#
# Preparing to start Appium
# - UDID is the device ID on which test will run and
#   required parameter on iOS test runs
# - appium - is a wrapper tha calls the latest installed
#   Appium server. Additional parameters can be passed
#   to the server here.
#
#########################################################

echo "UDID set to ${IOS_UDID}"
echo "Starting Appium ..."
appium -U ${IOS_UDID}  --log-no-colors --log-timestamp --command-timeout 120


#########################################################
#
# Setting of environment variables used later in test
# - used for Appium desired capabilities
# - note, APPIUM_URL is same for local and cloud server
#   runs
#########################################################
export APPIUM_APPFILE="$PWD/application.ipa"
export APPIUM_URL="http://localhost:4723/wd/hub"
export APPIUM_DEVICE="Local Device"
export APPIUM_PLATFORM="IOS"
export APPIUM_AUTOMATION="XCUITest"


## check iproxy
iproxy --version

## Start test execution
## Run the test:
echo "Running tests"
python3.7 -m pytest -s tests/ --junitxml=test-reports/report.xml

mv test-reports/*.xml TEST-all.xml
