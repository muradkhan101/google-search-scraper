import os
import argparse

from base64 import b64decode

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from helpers.wait import wait_for_load
from helpers.url import make_search_url
from helpers.directory import make_directories

ap = argparse.ArgumentParser(description='Scrape images from Google Images')
ap.add_argument('-q', '--query', required=True, help='Search term used to query Google Images')
ap.add_argument('-o', '--output', required=True, help='Directory to output images in')
ap.add_argument('-l', '--limit', type=int, default=25, help='Limit the number of images to scrape')
ap.add_argument('-r', '--resize', default=False, help='Set a max pixel length for larger side of the image')

# vars turns object into dictionary
args = vars(ap.parse_args())

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--window-size=1280x720")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0\ (Macintosh;\ Intel\ Mac\ OS\ X\ 10.12;\ rv:58.0)\ Gecko/20100101\ Firefox/58.0")

driver = webdriver.Chrome(executable_path=os.path.abspath(
    "bin/chromedriver"), chrome_options=chrome_options)

# https://www.google.com/search?tbm=isch&q=potato&oq=potato

url = make_search_url(args['query'])
driver.get(url)

images = driver.find_elements(By.TAG_NAME, 'img')


try:
    imagesGrabbed = 0
    if len(images) > 1:
        directory_path = args['output']
        make_directories(directory_path)
        for img in images[1:]:
            if imagesGrabbed + 1 > args['limit']:
                break
            imageUrl = img.get_attribute('src')
            if imageUrl != None:
                print(imageUrl)
                file_name = directory_path + '/' + args['query'] + '{0:03d}'.format(imagesGrabbed) + '.jpeg'
                # 23 is length of data:image/jpeg;base64, prepending string
                byte_array = b64decode(imageUrl[23:])
                with open(file_name, 'wb') as f:
                    f.write(byte_array)
                imagesGrabbed += 1
    else:
        print('No images found :0')
finally:
    driver.quit()

