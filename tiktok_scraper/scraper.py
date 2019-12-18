import os
import time

from tqdm import tqdm
from selenium.common.exceptions import ElementClickInterceptedException

from tiktok_scraper import ScrapeUtils, Wait, downloader

def create_folder_if_not_exist(folder):
  if not os.path.exists(folder):
    os.makedirs(folder)

def scrape_video(driver, folder="./"):
  url = driver.find_element_by_tag_name("video").get_attribute("src")
  name = "".join(url.split("/")[3:5])
  name = os.path.join(folder, name)
  downloader.download_mp4(name, url)
  ScrapeUtils.click_corner(driver)

def start(driver, username, folder=None, delay=1):
  if folder is None:
    folder = f"./{username}"
    create_folder_if_not_exist(folder)

  url = f"https://www.tiktok.com/@{username}"
  driver.get(url)
  if not Wait(driver).for_class_name("video-feed"):
    raise Exception(f"Can't load {url}")

  print("Getting all videos...")
  ScrapeUtils.scroll_bottom(driver)

  main_elem = driver.find_element_by_tag_name("main")
  print("Preparing to download")
  for link in tqdm(main_elem.find_elements_by_tag_name("a"), desc=f"Downloading videos to {folder}"):
    try:
      link.click()
    except ElementClickInterceptedException:
      print("clicked")
    except:
      print("failed")
    else:
      scrape_video(driver, folder=folder)
    time.sleep(delay)

if __name__ == "__main__":
  from selenium import webdriver
  driver = webdriver.Chrome("./chromedriver")
  start(driver, "edsheeran")
