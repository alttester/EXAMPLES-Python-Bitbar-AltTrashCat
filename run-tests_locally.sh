#!/bin/bash

##
## Work in progress! The dependency installations need to be done to the
## container so that we don't need to install them here.
##

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_121.jdk/Contents/Home

echo "Installing Appium Python Client 0.24 and xmlrunner 1.7.7"
chmod 0755 requirements.txt
pip install -r requirements.txt

echo "Starting Appium ..."

appium --log-no-colors --log-timestamp  --command-timeout 60  > appium.log 2>&1 &
sleep 10
ps -ef|grep appium
##### Cloud testrun dependencies end.

export APPIUM_APPFILE=$PWD/application.apk #App file is at current working folder

## Desired capabilities:

export APPIUM_URL="http://localhost:4723/wd/hub" # Local & Cloud
export APPIUM_DEVICE="Local Device"
export APPIUM_PLATFORM="android"


echo "Setting APPIUM_AUTOMATION=Appium"
export APPIUM_AUTOMATION="uiautomator2"

## Run the test:
echo "Running tests:"
rm -rf screenshots

python -m pytest tests/ --junitxml=test-reports/report.xml

killall node
