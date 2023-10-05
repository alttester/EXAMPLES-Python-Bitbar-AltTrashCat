### Running the tests on Android
You will first need to create an **.apk** file, with a build of your app containing the AltDriver.
[Here](https://alttester.com/walkthrough-tutorial-upgrading-trashcat-to-2-0-x/#Instrument%20TrashCat%20with%20AltTester%20Unity%20SDK%20v.2.0.x) is a helpful resource about the process of instrumenting the TrashCat application using AltTester Unity SDK `v2.0.2`.The build needs to be included under project and renamed with application.apk

### Running the tests on iOS
You will first need to create an **.ipa** file, with a build of your app containing the AltDriver.If you're unsure how to generate an **.ipa** file please watch the first half of [this video](https://www.youtube.com/embed/rCwWhEeivjY?start=0&end=199) for iOS.After you finish setting up the build, you need to use the **Archive** option to generate the standalone **.ipa**. The required steps for the archive option are described [here](https://docs.saucelabs.com/mobile-apps/automated-testing/ipa-files/#creating-ipa-files-for-appium-testing). Keep in mind that you need to select **Development** at step 6.The build needs to be included unzipped under project. Rename the app with application.apk
Reverse port forwarding is not working for iOS devices.
Workaround: Create TrashCat build with an Virtual Machine ip.This VM should keep AltTester Desktop.

**Steps to run the tests:**
1. Create a text file `license.txt` with your AltTester Desktop license.
2. From the cloned repository, run the *`create-bitbar-package.sh <ios|android>`* script, choosing your desired os as a parameter. This will create a **.zip** file, containing all the files required to execute the tests.

3. On BitBar, create a new project, and Select a target OS type (Android in our example) and a framework (Appium Server Side); 

4. Upload the application file (**.apk** or **.ipa**) and the **.zip** file. Please make sure to highlight both before clicking on *"Use selected"*. 
By default, the selected action for the zip file should be *“Use to run the test”* and for the app file *“Install on the device”*. If not, use the dropdown lists to select them. 

5. If you are using a free account, leave the *“Use existing device group”* option checked, together with *“Trial Android devices”* selected. As AltTester Desktop cannot handle multiple apps, you need to manually abort one device session. If you have a subscription, please see the BitBar Cloud documentation [here](https://docs.bitbar.com/testing/user-manuals/device-groups) for more info about creating your own device groups.

6. You can now create and run your automated tests.


Going back to the projects tab will allow you to monitor the progress of your tests and also show an overall status once the tests are done. Selecting an individual device will show you specific results for that device, as well as providing video recording of your test run.