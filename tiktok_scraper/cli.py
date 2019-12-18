#!/usr/bin/env python3
import os
from selenium import webdriver
import argparse
from tiktok_scraper import scraper

def get_chromedriver(driver_location, show_browser=False, has_driver=False):
  from selenium.webdriver.chrome.options import Options
  chrome_options = Options()
  if not show_browser:
    chrome_options.add_argument("--headless")
  if has_driver:
    return webdriver.Chrome(options=chrome_options)
  else:
    return webdriver.Chrome(driver_location, options=chrome_options)

def main(driver_location="./chromedriver", driver=None, has_driver=False):
  parser = argparse.ArgumentParser()
  parser.add_argument("username", help="The TikTok username", type=str)
  parser.add_argument("--driver", help="Driver location", type=str)
  parser.add_argument("--driver-type", help="Type of driver (i.e. Chrome)", type=str)
  parser.add_argument("--show-browser", help="Shows browser while scraping. Useful for debugging", action="store_true")
  parser.add_argument("--delay", type=int, help="Number of seconds to delay between video downloading", default=0)
  parser.add_argument("--location", help="Location to store the files")

  args = parser.parse_args()

  if not args.driver:
    if not os.path.isfile(driver_location):
      try:
        webdriver.Chrome()
        has_driver = True
      except:
        import AutoChromedriver
        AutoChromedriver.download_chromedriver()
  else:
    driver_location = args.driver

  if not args.driver_type:
    driver = get_chromedriver(driver_location, show_browser=args.show_browser, has_driver=has_driver)
  else:
    if args.driver_type.lower() == 'chrome':
      driver = get_chromedriver(driver_location, show_browser=args.show_browser, has_driver=has_driver)
    if args.driver_type.lower() == 'firefox':
      driver = webdriver.Firefox()

  scraper.start(driver, args.username, folder=args.location, delay=args.delay)


if __name__ == "__main__":
  main()
