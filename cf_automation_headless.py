
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from time import sleep



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)



def scrape_top_news():
    i = 0
    while i < 5:
        driver.get('https://fast.com')
        sleep(9)
        speed= driver.find_element_by_xpath('//*[@id="speed-value"]')
        name= driver.find_element_by_xpath('//*[@id="speed-units"]')
        speed_number = speed.text
        speed_name = name.text
        print(str(speed_number)+str(speed_name) + '  '+str(i))
        i += 1


scrape_top_news()





