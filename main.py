from selenium import webdriver
from time import sleep



# define the web driver
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options, executable_path=r'/Users/mohammadsolaiman/Documents/chromedriver')
driver.implicitly_wait(10)

i = 0
while i < 40:
    driver.get('https://fast.com')
    sleep(9)
    speed= driver.find_element_by_xpath('//*[@id="speed-value"]')
    name= driver.find_element_by_xpath('//*[@id="speed-units"]')
    speed_number = speed.text
    speed_name = name.text
    print(str(speed_number)+str(speed_name) + '  '+str(i))
    i += 1