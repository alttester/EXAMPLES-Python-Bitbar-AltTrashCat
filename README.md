This demo project contains a pre-built ***ipa*** and ***apk*** file, so you can try out running tests on both Android and iOS

### Running the tests on Android
The app is provided at https://altom.com/app/uploads/AltTester/TrashCat/TrashCatAndroid.zip and needs to be included unzipped under project. Rename yhe app with application.apk

### Running the tests on iOS
Reverse port forwarding is not working for iOS devices.
Workaround: Create TrashCat build with an VM ip.This VM should keep AltTester Desktop.

**Steps to run the tests:**
1. Create a text file `license.txt` under project and write your AltTester Desktop license.
2. From the cloned repository, run the *`create-bitbar-package.sh <ios|android>`* script, choosing your desired os as a parameter. This will create a **.zip** file, containing all the files required to execute the tests.

3. On BitBar, create a new project, and Select a target OS type (Android in our example) and a framework (Appium Server Side); 

4. Upload the application file (**.apk** or **.ipa**) and the **.zip** file. Please make sure to highlight both before clicking on *"Use selected"*. 
By default, the selected action for the zip file should be *“Use to run the test”* and for the app file *“Install on the device”*. If not, use the dropdown lists to select them. 

5. If you are using a free account, leave the *“Use existing device group”* option checked, together with *“Trial Android devices”* selected. As AltTester Desktop cannot handle multiple apps, you need to manually abort one device session. If you have a subscription, please see the BitBar Cloud documentation [here](https://docs.bitbar.com/testing/user-manuals/device-groups) for more info about creating your own device groups.

6. You can now create and run your automated tests.


Going back to the projects tab will allow you to monitor the progress of your tests and also show an overall status once the tests are done. Selecting an individual device will show you specific results for that device, as well as providing video recording of your test run.