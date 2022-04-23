from selenium import webdriver
from pyquery import PyQuery as pq
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

#load webpage
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url='https://zfwzzc.www.gov.cn/check_web/databaseInfo/download#page-1'
driver.get(url)

#click one department (five deps at a time)
xpath_dep = '/html/body/div[4]/div[2]/ul/li[1]/div' #change li[1] 
driver.find_element(by=By.XPATH, value=xpath_dep).click() #click to select dep

#click to download
xpath_download = '/html/body/div[4]/div[2]/div[1]/div[2]' #click download button
driver.find_element(by=By.XPATH, value=xpath_download).click()




#page 1
#国务院
#地方政府

#click download
