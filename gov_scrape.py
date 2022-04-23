from selenium import webdriver
import re
from pyquery import PyQuery as pq
import xlwt
import xlrd
import time
from selenium.webdriver.chrome.options import Options
import string
import time
import requests,random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#load webpage
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
# to supress the error messages/logs
options.add_experimental_option('excludeSwitches', ['enable-logging'])
url='https://zfwzzc.www.gov.cn/check_web/databaseInfo/download#page-1'
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get(url)

#click one department (five deps at a time)
xpath_dep = '/html/body/div[4]/div[2]/ul/li[1]/div' #change li[1] 
browser.find_element(by=By.XPATH, value=xpath_dep).click() #click to select dep
#error code:handshake failed; returned -1, SSL error code 1, net_error -101




#page 1
#国务院
#地方政府

#click download
