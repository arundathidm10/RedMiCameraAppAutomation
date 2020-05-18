import time
from CameraAppAutomationRedMi import AppLaunch_Camera as al
from CameraAppAutomationRedMi import TestCase_01 as tc1

'''
Test Case to delete the captured Image
'''

time.sleep(3)
# al.driver.back()
al.driver.press_keycode(4)
print("Clicked on Back button successfully")
time.sleep(2)
# clicking on delete button
al.driver.find_element_by_xpath("//*[@text='Delete' and @package='com.miui.gallery']").click()
time.sleep(2)
al.driver.find_element_by_id("android:id/button1").click()
print("Image deleted successfully")
time.sleep(1)
al.driver.back()
al.driver.close_app()
print("App closed successfully")