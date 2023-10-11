#!/bin/bash

## Cloud testrun dependencies start
echo "Extracting tests.zip..."
unzip tests.zip

echo "Installing pip requirements"
chmod 0755 requirements.txt
apt-get --assume-yes install python3.10
python3.10 --version
python3.10 -m pip install --upgrade pip
python3.10 -m pip install wheel
python3.10 -m pip install -r requirements.txt
python3.10 -m pip list

## Environment variables setup
echo "UDID set to ${IOS_UDID}"
export APPIUM_PORT="4723"
export APPIUM_AUTOMATION="XCUITest"
export APPIUM_APPFILE="$PWD/TrashCat.ipa"

## Appium server launch
echo "Starting Appium ..."
appium -U ${IOS_UDID} --log-no-colors --log-timestamp --command-timeout 120
ps -ef|grep appium

## Run the test:
echo "Running tests"
rm -rf screenshots
python3.10 -m pytest -s tests/ --junitxml=test-reports/report.xml

mv test-reports/*.xml TEST-all.xml
