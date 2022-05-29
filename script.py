from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
import time

file = open('s.txt')
lines = file.readlines()
lines_1 = []
with open('ss.txt', 'a') as f:
    for i in lines:
        q = i.replace(' ','+')
        url = 'https://www.youtube.com/results?search_query='+q
        options = ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(0.4)
        element = driver.find_elements(by=By.CLASS_NAME, value='match-page')
        element = driver.find_elements(by=By.CLASS_NAME, value='style-scope ytd-video-renderer')
        hr = element[0].find_element(by=By.ID, value="video-title").get_attribute('href')
        print(hr)
        f.write(f'{hr}\n')
        driver.quit()
    
    
