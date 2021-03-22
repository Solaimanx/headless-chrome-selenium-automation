import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# driver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

#code start here


driver.get('http://google.com/')
search = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
search.click()
sleep(2)

driver.execute_script("arguments[0].value='קונפידנס - לדבר אנגלית, לא לגמגם. '",search)

sleep(3)
search_button = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]')
search_button.click()
sleep(3)
driver.find_element_by_xpath('//*[@id="rso"]/div[2]/div[1]/div/div[1]/a/h3/span').click()
sleep(4)
text = driver.find_element_by_xpath('//*[@id="ArticleHeaderComponent"]/div[2]/h1')
text_ = text.getText()
print(text_)
driver.save_screenshot("screenshot.png")
print('done check the screenshort')










