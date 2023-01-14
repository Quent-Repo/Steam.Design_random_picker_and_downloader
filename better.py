# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import random
import shutil
import datetime

x=datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#M##akes Files to store the image picked and the name of image in a .txt file.
if(os.path.exists("File") != True):
    os.mkdir("File")
os.mkdir(os.path.join("File",x))


options = Options()
options.headless = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

###Change the location of where the download will go.
#prefs = {'download.default_directory' : r'C:\Users\kjgdf\Desktop\simplify6\File\\'}
#options.add_experimental_option('prefs', prefs)

###Change the location to where your browser driver is.
service = Service(executable_path="C:/Users/kjgdf/Desktop/chromedriver.exe")
browser = webdriver.Chrome(service=service, options=options)
print("Program is running")
browser.get('http://steam.design')
assert 'Steam.Design' in browser.title
browser.minimize_window()
location = os.getcwd()

###Gets buttion and clicks it
elem = browser.find_element(By.CLASS_NAME, "menu__window-button-text")
time.sleep(4)
elem.click()
browser.minimize_window()
page_url = browser.current_url
print("Program is getting background")




###akes list of every file in the folder
List_Of_Files = os.listdir()
###Randomly picks an image. 3 is the folder we just made. -1 if for the .py file that is doing all the work.
Number_Picked_From_List = random.randint(3, len(List_Of_Files)-1)
File_Name = List_Of_Files[Number_Picked_From_List]
shutil.copy(List_Of_Files[Number_Picked_From_List], os.path.join("File",x))
###Opens the image that has been picked.
#os.startfile(List_Of_Files[Number_Picked_From_List])

###Changes directoy to File and makes the .txt file.
os.chdir(os.path.join("File",x))
print("Making text file")
f = open("url_for_background.txt", "w")
f.write(page_url + "\n")
f.write(File_Name)
f.close()
print("Finished")

###Closes browser
time.sleep(5)
browser.quit()


