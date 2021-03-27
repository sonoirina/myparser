from selenium import webdriver
from time import sleep


driver=webdriver.Chrome('C://Users/roman/AppData/Local/Programs/Python/Python37-32/Lib/site-packages/selenium/common/chromedriver_win32 (1)/chromedriver.exe')
driver.get('https://upakovka-spb.ru/category/2-odnorazovaya-posuda/11-kontyeynyery/')
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

images = driver.find_elements_by_css_selector('img[src*=svg]')
for _ in images:
    print(_.get_attribute("alt"))
