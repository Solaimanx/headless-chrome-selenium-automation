
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)



def scrape_top_news():

    wait = WebDriverWait(driver, 10)
    driver.get('https://news.ycombinator.com/')
    element_list = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".title > a"))
    )
    for element in element_list:
        try:
            url = element.text 
            title = element.get_attribute('href')
            print("Title:" + str(title) + '\nURL:' + str(url) + '\n\n')
        except Exception as e:
            print(e)
    time.sleep(2)
    driver.quit()


if __name__ == '__main__':
    scrape_top_news()





