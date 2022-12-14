#!/bin/bash

## Environment variables setup
export PLATFORM_NAME="Android"
export UDID=${ANDROID_SERIAL}
export APPIUM_PORT="4723"

APILEVEL=$(adb shell getprop ro.build.version.sdk)
APILEVEL="${APILEVEL//[$'\t\r\n']}"
export PLATFORM_VERSION=${APILEVEL}
echo "API level is: ${APILEVEL}"
if [ "$APILEVEL" -gt "19" ]; then
	export AUTOMATION_NAME="UiAutomator2"
	echo "UiAutomator2"
else
	export AUTOMATION_NAME="UiAutomator1"
	echo "UiAutomator1"
fi

TEST=${TEST:="SampleAppTest"}

##### Cloud testrun dependencies start
echo "Extracting tests.zip..."
unzip tests.zip

echo "Installing pip requirements"
chmod 0755 requirements.txt
apt-get --assume-yes install python3.7
python3 --version
python3.7 --version
python3.7 -m pip install --upgrade pip
python3.7 -m pip install wheel
python3.7 -m pip install -r requirements.txt
python3.7 -m pip list

echo "Starting Appium ..."
appium --log-no-colors --log-timestamp  --command-timeout 60  > appium.log 2>&1 &

ps -ef|grep appium
##### Cloud testrun dependencies end.

export APPIUM_APPFILE=$PWD/application.apk #App file is at current working folder

## Run the test:
echo "Running tests"
rm -rf screenshots
python3.7 -m pytest -s tests/ --junitxml=test-reports/report.xml

mv test-reports/*.xml TEST-all.xml