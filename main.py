from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
import os
import shutil


x=time.asctime()

#Made so the browser does not show
#options = FirefoxOptions()
#options.add_argument("--headless")
#Key
#browser = webdriver.Firefox(options=options)
browser = webdriver.Firefox()



os.mkdir(x)
browser.get('http://steam.design')
assert 'Steam.Design' in browser.title
#Gets buttion and clicks it
elem = browser.find_element(By.CLASS_NAME, "menu__window-button-text")# Find the search box
time.sleep(4)
elem.click()
print(browser.current_url)
#stores the url in txt


#moves txt to new folder
#shutil.copy("url_for_background.txt", str(x)) #use this to copy image files over
os.chdir(x)
f = open("url_for_background.txt", "w")
f.write(browser.current_url)
f.close()

time.sleep(10)
browser.quit()