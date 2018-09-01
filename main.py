import os
import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from helpers.wait import wait_for_load
from helpers.url import make_search_url

ap = argparse.ArgumentParser(description='Scrape images from Google Images')
ap.add_argument('-q', '--query', required=True, help='Search term used to query Google Images')
ap.add_argument('-o', '--output', required=True, help='Directory to output images in')
ap.add_argument('-l', '--limit', type=int, default=25)

# vars turns object into dictionary
args = vars(ap.parse_args())

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument("--window-size=1280x720")
# chrome_options.add_argument(
#     "user-agent=Mozilla/5.0\ (Macintosh;\ Intel\ Mac\ OS\ X\ 10.12;\ rv:58.0)\ Gecko/20100101\ Firefox/58.0")

# driver = webdriver.Chrome(executable_path=os.path.abspath(
#     "src/bin/chromedriver"), chrome_options=chrome_options)

# # https://www.google.com/search?tbm=isch&q=potato&oq=potato

# driver.get(make_search_url())