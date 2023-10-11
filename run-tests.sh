#!/bin/bash
echo "==> Setup ADB port reverse..."
adb reverse --remove-all
adb reverse tcp:13000 tcp:13000

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


## Appium server launch
echo "Starting Appium ..."
appium --log-no-colors --log-timestamp  --command-timeout 60  > appium.log 2>&1 &
ps -ef|grep appium

export LICENSE_KEY=$(cat license.txt)

Install and launch AltTester Desktop
brew install wget
wget https://alttester.com/app/uploads/AltTester/desktop/AltTesterDesktopLinuxBatchmode.zip
unzip AltTesterDesktopLinuxBatchmode.zip
cd AltTesterDesktopLinux


## Start AltTester Desktop from batchmode
echo "Starting AltTester Desktop ..."

chmod +x ./AltTesterDesktop.x86_64
./AltTesterDesktop.x86_64 -batchmode -port 13000 -license $LICENSE_KEY -nographics -termsAndConditionsAccepted &
cd ..

## Run the test:
echo "Running tests"
rm -rf screenshots
python3.10 -m pytest -s tests/ --junitxml=test-reports/report.xml

mv test-reports/*.xml TEST-all.xml

echo "Deactivate AltTesterDesktop license"
cd AltTesterDesktopLinux
kill -2 `ps -ef | awk '/AltTesterDesktop.x86_64/{print $2}'`
sleep 10
./AltTesterDesktop.x86_64 -batchmode -nographics -removeActivation