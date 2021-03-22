import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pickle


# driver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

#code start here



#veriables to track activity in terminal
link_list = []
footer_found = 0
footer_didnt_found = 0
logo_found = 0
logo_didnt_found = 0
seo_found = 0
total = 0


username ='info@ericniceberg.com'
password = 'xJL3E6PJCQkj3yx'


#get cookis from website
def get_cookies():
    driver.get('https://infoa9bf3f-app.clickfunnels.com/users/sign_in')
    driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="user_password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()
    driver.find_element_by_xpath('//*[@id="loginfields"]/div[4]/input').click()
    pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    print('store the chookies successfully')
    sleep(8)



#login 
def login_with_cookies():
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    print('login successfully')
    sleep(10)


def change_image(link):
    global logo_found
    global logo_didnt_found
    driver.get(link)
    #Click "edit Page"
    sleep(10)
    driver.find_element_by_xpath("(//a[contains(@class,'btn btn-warning openPageInEditor')])[1]").click()
    sleep(10)
    #check if there are any logo
    #b1
    try:
        #black logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/04/c9f6a8e0b34daebb44ddbdf3dd7d97/FinalLogoDark_600px_2021.png')]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div/input')[1]
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/8a/39d718264b4782bd5712737494a73b/ConfiLogoBLACK.png')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()

        logo_found += 1
        sleep(10)
    except:
        logo_didnt_found += 1
    #b2
    try:
        #black logo
        logo = driver.find_element_by_xpath("//img[contains(@src,https://images.clickfunnels.com/24/c0c405488c4ffba57a8cce8e2e5750/FinalLogoDark.png)]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div/input')[1]
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/8a/39d718264b4782bd5712737494a73b/ConfiLogoBLACK.png')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()

        logo_found += 1
        sleep(10)
    except:
        logo_didnt_found += 1
    #w1
    try:
        #white logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/8a/083c5adb0540b89a761f7b49f12e7f/FinalLogoWhite_600px.png')]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()

        logo_found += 1
        sleep(10)
    except:
        logo_didnt_found += 1
    #w2
    try:
        #white logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/94/7774b1d84a44ea840f760845e5866f/FinalLogoWhite_600px_2021.png')]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()

        logo_found += 1
        sleep(10)
    except:
        logo_didnt_found += 1
    #w3
    try:
        #white logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/40/4531a937d54d34ae992a5e2903e15e/FinalLogoWhite_250px.png')]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()

        logo_found += 1
        sleep(10)
    except:
        logo_didnt_found += 1
    #w4
    try:
        #white logo
        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/07/14e3432cd143be9db53277071d205e/FinalLogoWhite.png')]")
        logo.click()
        #click on advance settings
        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
        advance_settings.click()
        #image input field
        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
        sleep(1)
        img_input.clear()
        sleep(1)
        img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
        #close settings and Save
        driver.find_element_by_xpath('/html/body/div[11]').click()
        driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()

        logo_found += 1
        sleep(10)
    except:
        logo_didnt_found += 1
        

def footer_remove_and_add():
    global footer_found
    global footer_didnt_found
    sleep(3)
    try:
        try:
            footer = driver.find_element_by_xpath("//div[contains(text(),'לדבר אנגלית ב 21 יום')]")
        except:
            sleep(1)
        try:
            footer = driver.find_element_by_xpath("//div[contains(text(),'אנגלית ב 21 יום')]")
        except:
            sleep(1)
        hover = ActionChains(driver).move_to_element(footer)
        hover.perform()
        #hoverover on to show the settings
        move_little_up = ActionChains(driver).move_by_offset(50,20)
        move_little_up.perform()
        sleep(1)
        #click on remove and accept alert
        remove_section = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools-section')][not(contains(@style,'display: none'))][contains(@style,'opacity: 1')]/div/div[contains(@class,'de-rollover-remove-section')]")
        remove_section.click()
        sleep(1)
        alert = driver.switch_to.alert
        alert.accept()
        sleep(1)
        # add new footer 
        drag_and_drop()
        footer_found += 1

    except:
        footer_didnt_found += 1



def drag_and_drop():
    section = driver.find_element_by_xpath("//div[contains(@class,'editorTopNavItemX editorTopNavItemShowSub pull-left')]/span[contains(text(),'Sections')]")
    hover_section = ActionChains(driver).move_to_element(section)
    hover_section.perform()
    add_section = driver.find_element_by_xpath("/html/body/div[68]/div[2]/div[1]/div[1]/div/div[1]")
    add_section.click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="personalSections"]').click()
    sleep(2)
    # drag and drop source and targets elements
    drag = driver.find_element_by_xpath('//*[@id="personal_section_templates"]/div[1]')
    drop = driver.find_elements_by_xpath("//div[contains(@class,'dropZoneForSections ui-droppable')]")[-1]
    drog__drop = ActionChains(driver).click_and_hold(drag).pause(5).move_by_offset(-30,10).pause(3).move_to_element(drop).release(drop)
    drog__drop.perform()
    #save
    driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
    sleep(13)



def seo_meta_tag():
    global seo_found
    sleep(3)
    settings = driver.find_element_by_xpath('//*[@id="editorTopNav_settings"]')
    hover_settings = ActionChains(driver).move_to_element(settings)
    hover_settings.perform()
    #click on settings > Seo meta data
    add_seo_meta_tag = driver.find_element_by_xpath('//*[@id="editorTopNav_settings"]/div/div[2]')
    add_seo_meta_tag.click()
    sleep(2)
    #meta data
    seo_meta_data = driver.find_element_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div[3]/input')
    seo_meta_data.clear()
    seo_meta_data.click()
    driver.execute_script("document.getElementById('edit-seo-title').value='קונפידנס - לדבר אנגלית, לא לגמגם. '")
    #description
    seo_description = driver.find_element_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div[4]/textarea')
    seo_description.clear()
    seo_description.click()
    driver.execute_script("document.getElementById('edit-seo-desc').value='קונפידנס - לדבר אנגלית, לא לגמגם. '")
    sleep(1)
    #keywards
    seo_keywards = driver.find_element_by_xpath('//div[contains(@class,"editorSectionInner editSEOSetings")]/div[5]/input')
    seo_keywards.clear()
    seo_keywards.click()
    driver.execute_script("document.getElementById('edit-seo-keywords').value='קונפידנס - לדבר אנגלית, לא לגמגם. '")
    sleep(1)
    #close settings and Save
    driver.find_element_by_xpath('/html/body/div[11]').click()
    driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
    seo_found += 1
    sleep(10)


def collect_all_link():
    global link_list
    ###collect from link from side bar 
    link_funnel_step = driver.find_elements_by_xpath("//div[contains(@class,'funnel_step')]/div/a")
    for every_funnel_step_link in link_funnel_step:
        new_link = every_funnel_step_link.get_attribute("href")
        link_list.append(new_link)
        print(new_link)

    #collect link from dropdown 
    dropdown_link = driver.find_elements_by_xpath('//*[@id="other_steps"]/option')
    for every_dropdown_link in dropdown_link:
        new_links = every_dropdown_link.get_attribute("value")
        final_link = 'https://infoa9bf3f-app.clickfunnels.com'+str(new_links)
        link_list.append(final_link)
        print(final_link)

def main():
    global total
    # get_cookies()
    login_with_cookies()
    collect_all_link()
    print('collected all link')
    print(link_list)
    # try:
    #     link_list.remove('https://infoa9bf3f-app.clickfunnels.com')
    # except:
    #     sleep(1)
    # for page_link in link_list:
    #     change_image(page_link)
    #     seo_meta_tag()
    #     footer_remove_and_add()
    #     total += 1
    #     print('_____________________________________________')
    #     print('Pages check done =======>  '+ str(total))
    #     print('Logo added =====> '+str(logo_found)+ '\n' +'Logo checked found  =====> '+str(logo_didnt_found) + '\n'+ 'footer added =====> '+str(footer_found)+'\n'+ 'Foodter didn\'t found  =====> '+ str(footer_didnt_found) +'\n' +'SEO added =====> '+str(seo_found))



#start here
main()