import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





class YouTubePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_button = (AppiumBy.ACCESSIBILITY_ID,"Search")
        self.search_box = (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.google.android.youtube:id/search_edit_text']")


    def click_search_button(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.search_button))
        self.driver.find_element(*self.search_button).click()

    def click_search_box(self,search_text):
        wait=WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(self.search_box))
        self.driver.find_element(*self.search_box).send_keys(search_text)
        self.driver.press_keycode(66)



