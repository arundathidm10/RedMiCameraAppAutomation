import time
from CameraAppAutomationRedMi import AppLaunch_Camera as al

'''
Test Case to Enable Front Camera & Capture Image in Front Camera Mode
'''

time.sleep(2)
# Enabling Front Camera
al.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Front and rear camera switch']").click()
print("Enabled Image Capture in Front Camera Mode")
time.sleep(3)
# clicking on Shutter button to capture image in HDR Mode
al.driver.find_element_by_id("com.android.camera:id/v6_shutter_button_internal").click()
print("Image captured successfully in Front Camera Mode")
time.sleep(3)
al.driver.close_app()
print("App closed successfully")