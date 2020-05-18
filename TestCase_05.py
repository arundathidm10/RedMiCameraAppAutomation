import time
from CameraAppAutomationRedMi import AppLaunch_Camera as al

'''
Test Case to turn on Video Mode & Capture Video
'''

time.sleep(2)
# Enabling Video Mode
al.driver.find_element_by_id("com.android.camera:id/v6_module_picker").click()
print("Enabled Video Mode")
time.sleep(3)
# clicking on Shutter button to capture Video
al.driver.find_element_by_id("com.android.camera:id/v6_shutter_button_internal").click()
print("Video Capturing Started")
time.sleep(8)
al.driver.find_element_by_id("com.android.camera:id/v6_shutter_button_internal").click()
print("Stopped Video capturing after 8 seconds.. Video Saved")
time.sleep(3)
al.driver.close_app()
print("App closed successfully")