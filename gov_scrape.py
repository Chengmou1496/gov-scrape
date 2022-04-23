from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

#load webpage
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
url='https://zfwzzc.www.gov.cn/check_web/databaseInfo/download#page-1'
driver.get(url)


#count how many li[x] in this page
count = len(driver.find_elements_by_xpath("/html/body/div[4]/div[2]/ul//li/div")) #can count the total number at all pages
max_group = int(count/5) #13 groups in total

for j in range(max_group): #0-12
    start_index = 1+5*j
    end_index = start_index+4

    for i in range(start_index,end_index+1):#start and end indicated
        #click one department
        xpath_dep= '/html/body/div[4]/div[2]/ul/li['+str(i)+']/div'
        driver.find_element(by=By.XPATH, value=xpath_dep).click() #click to select dep
        #click to download
        xpath_download = '/html/body/div[4]/div[2]/div[1]/div[2]' #click download button
        driver.find_element(by=By.XPATH, value=xpath_download).click()
    
    #reload the page to reclick department
    driver.refresh()





#page 1
#国务院
#地方政府

#click download
