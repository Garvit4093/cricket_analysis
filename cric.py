import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options=Options()
s=Service("C:\chromedriver.exe")
driver = webdriver.Chrome(service=s,options=options)
url="https://www.cricbuzz.com/live-cricket-full-commentary/75486/rsa-vs-ned-15th-match-icc-cricket-world-cup-2023"
driver.get(url)
button=driver.find_elements(By.CLASS_NAME,"cb-nav-pill-1")
button[1].click()
time.sleep(5)
# ball number over
soup=BeautifulSoup(driver.page_source,'html.parser')
# WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME,'cb-mat-mnu-wrp')))
# list=soup.find_all('div',{'class':'cb-mat-mnu-wrp'})
# for item in list:
#     print(item.get_text())
WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME,'cb-com-ln')))
list=soup.find_all('p',{'class':'cb-com-ln'})
i=0
for item in list:
    i=i+1
    if(i>4):
      print(item.get_text())
driver.close()