from appium import webdriver
global driver

'''
Test Case to launch Camera Application
'''
# adb command to identify the AppPackage & AppActivity
# adb shell "dumpsys window windows | grep -E 'mCurrentFocus'"
desired_caps = {
    "platformName": "Android",
    "deviceName": "Redmi",
    "noReset": True,
    "udid": "203a43ac7ce4",
    "noSign": True,
    "autoGrantPermissions": True,
    "automationName": "UiAutomator2",
    "platformVersion": "7.1.2",
    "appPackage": "com.android.camera",
    "appActivity": "com.android.camera.Camera"
}
driver = webdriver.Remote("http://127.0.0.1:4586/wd/hub", desired_caps)
driver.implicitly_wait(30)
print("Camera App Launched successfully")
