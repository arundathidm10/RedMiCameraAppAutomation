import time
from CameraAppAutomationRedMi import AppLaunch_Camera as al

'''
Test Case to capture Image with Camera App and checking the details of captured Image
'''

time.sleep(2)
#  clicking on Shutter button to capture image
al.driver.find_element_by_id("com.android.camera:id/v6_shutter_button_internal").click()
print("Image captured successfully")
time.sleep(3)
# clicking on captured image
al.driver.find_element_by_id("com.android.camera:id/v6_thumbnail_image").click()
al.driver.find_element_by_id("com.miui.gallery:id/photoview").click()
# clicking on Menu button
al.driver.find_element_by_xpath("//*[@text='More' and @package='com.miui.gallery']").click()
print("Clicked on Menu button successfully")
time.sleep(2)
# clicking on Details option
al.driver.find_element_by_xpath("//android.widget.TextView[@text='Details']").click()
print("Clicked on Details button successfully")
# Checking the image captured date and asserting into it
date = al.driver.find_element_by_xpath("//android.widget.TextView[@text='4 May, 2020']")
print("Image details were displayed successfully")
assert date.text == "4 May, 2020"
print("Captured on 4th May 2020...  It's Perfect ")
al.driver.save_screenshot("../Image_details.png")
print("Captured Screenshot of Image details and Stored it")