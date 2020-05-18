import time
from CameraAppAutomationRedMi import AppLaunch_Camera as al

'''
Test Case to Enable HDR Mode & Capture Image in HDR Mode
'''

time.sleep(2)
# Enabling HDR Mode
al.driver.find_element_by_id("com.android.camera:id/v6_hdr").click()
print("Enabled Image Capture in HDR Mode")
time.sleep(3)
# clicking on Shutter button to capture image in HDR Mode
al.driver.find_element_by_id("com.android.camera:id/v6_shutter_button_internal").click()
print("Image captured successfully in HDR Mode")
time.sleep(3)
al.driver.close_app()
print("App closed successfully")