from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep, strftime
from random import randint, random
import pandas as pd

#for chromedriver
chromedriver_path ='/Users/xxx/chromedriver' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(1)
action = ActionChains(webdriver)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)

hashtag_list = ['hope', 'puppy', 'love'] # Change this to your own tags

username = webdriver.find_element_by_name('username')
username.send_keys('aaaaaaaaa') # Change this to your own Instagram username
password = webdriver.find_element_by_name('password')
password.send_keys('aaaaaaaaa') # Change this to your own Instagram password

def mouse_move_and_click(driver,element):
    sleep(randint(1,6))
    print("in function")
    action = ActionChains(webdriver)
    action.move_to_element(element).perform()
    action.click(element).perform()
    print("out function")

def mouse_move_and_Dclick(driver,element):
    sleep(randint(1, 6))
    print("in function2")
    action = ActionChains(webdriver)
    action.move_to_element(element).perform()
    action.double_click(element).perform()
    print("out function2")


#find login button
button_login = webdriver.find_element_by_xpath('//html//body//div[1]//section//main//div//article//div//div[1]//div//form//div//div[3]//button//div')

mouse_move_and_click(webdriver, button_login)

sleep(5)

dontsave = webdriver.find_element_by_xpath('//html/body/div[1]/section/main/div/div/div/div/button')

mouse_move_and_click(webdriver,dontsave)

sleep(5)

dontshownotifications = webdriver.find_element_by_xpath('//html/body/div[4]/div/div/div/div[3]/button[2]')

mouse_move_and_click(webdriver,dontshownotifications)


# DB connection
client = MongoClient('mongodb://user:Password1@127.0.0.1/mongodb', 1111) #enter user, password for mongo db with users list 1111 change to port number
db = client.main
collection = db.insta

allDB = 0
allDB = collection.find({})

for i in range(1, 100):
    userID = allDB[i]['_id']
    print("Checking user: " + allDB[i]['user_name'])
    sleep(randint(2,6))
    webdriver.get('https://www.instagram.com/' + allDB[i]['user_name'])
    try:
        photo3 = webdriver.find_element_by_xpath('//html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[3]/a/div/div[2]')
        mouse_move_and_click(webdriver,photo3)
        like = webdriver.find_element_by_class_name('_9AhH0')
        mouse_move_and_Dclick(webdriver,like)
    except:
        pass
