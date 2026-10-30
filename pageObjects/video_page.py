from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import TimeoutException



class VideoPage:
    def __init__(self, driver):
        self.driver = driver
        self.python_video = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Python Full Course for Beginners - 2 hours, 2 minutes, 21 seconds - Go to channel Programming with Mosh - Programming with Mosh - 8 million views - 1 year ago - play video']/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]")
        self.skip_button = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.google.android.youtube:id/skip_ad_button_text']")
        self.close_video = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Course - Python for Beginners (Full Course) | #100DaysOfCode Programming Tutorial in Hindi - CodeWithHarry - 100 videos']/android.view.ViewGroup[4]/android.widget.ImageView[@content-desc='Action menu']")
        self.next_video = (AppiumBy.XPATH, "//android.view.ViewGroup[@content-desc='Course - Python Ultimate Course - Data with Baraa - 47 videos']/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.ImageView[1]")




    def click_python_video(self):
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.python_video))
        self.driver.find_element(*self.python_video).click()

    def skip_ad_if_present(self):
        try:
            wait=WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.skip_button))
            self.driver.find_element(*self.skip_button).click()
            print("skip button clicked successfully")
        except TimeoutException:
            print("no skip button found")

    def go_back_to_results(self):
        self.driver.back()
        time.sleep(5)

    def close_play_video(self):
        self.driver.find_element(*self.close_video).click()

    def scroll_results(self):
        self.driver.execute_script(
            "mobile: scrollGesture",
            {
                 "left": 0,
                 "top": 100,
                 "width": 480,
                 "height": 700,
                 "direction": "down",
                 "percent": 0.75
            }
        )
        time.sleep(5)

    def click_next_video(self):
        self.driver.find_element(*self.next_video).click()