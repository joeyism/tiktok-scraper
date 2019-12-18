import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class ScrapeUtils:

  @classmethod
  def move_down(cls, driver, by=0.25):
    driver.execute_script(f"window.scrollTo(0, Math.ceil(document.body.scrollHeight*{by}));")

  @classmethod
  def click_corner(cls, driver):
    action = webdriver.ActionChains(driver)
    action.move_by_offset(1, 1)
    action.click()
    action.perform()

  @classmethod
  def scroll_bottom(cls, driver, SCROLL_PAUSE_TIME=2):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
      driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(SCROLL_PAUSE_TIME)
      new_height = driver.execute_script("return document.body.scrollHeight")
      if new_height == last_height:
        break
      last_height = new_height

class Wait:

  def __init__(self, driver):
    self.driver = driver

  def for_id(self, id, delay=3):
    try:
      WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, id)))
      return True
    except TimeoutException:
      return False

  def for_class_name(self, class_name, delay=3):
    try:
      WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
      return True
    except TimeoutException:
      return False
