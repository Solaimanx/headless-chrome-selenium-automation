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
chrome_options.add_argument("--window-size=1700,1000")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36')
chrome_options.add_argument("--no-sandbox")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver.implicitly_wait(25)


link_list = [
 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/57757707/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/58492462/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/58511172/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/64145502/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/58536033/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44815989/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59241840/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59242582/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44815998/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44815999/overview',
 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816009/overview', 
'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816010/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50676146/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50676166/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816011/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816015/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816017/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816022/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816027/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816034/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816039/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816043/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816044/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50596676/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50596771/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50597339/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50597421/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50597809/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50597909/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50598024/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50598081/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50598253/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50598298/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816048/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50453594/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50676658/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/63573473/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/63573493/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/63573496/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816049/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816052/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50639311/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50663626/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816053/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816054/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816055/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816057/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44816086/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/49669398/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/49671358/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53071620/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53068883/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/44815997/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50435517/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50742359/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50742415/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50742470/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50742510/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50742656/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50742739/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50743464/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50743585/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50743617/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50743754/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50743900/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744207/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744262/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744292/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744338/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744382/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744416/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50744750/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50746758/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50749699/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50773265/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50875211/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53138487/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53713690/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53721254/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53721398/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53721626/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53721797/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53721915/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53722096/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53723213/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53723338/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53723537/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53723708/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53724197/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53724515/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53724881/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53725002/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53725151/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53725345/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53725460/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53726362/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53726808/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53726989/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53727188/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53863346/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53863471/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53863510/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53863551/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53863611/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53903324/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53907350/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53908493/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53910305/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53912259/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53926270/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53926642/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53927158/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53927341/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53928389/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53929480/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53929726/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53930153/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53930750/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53931206/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53931439/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53931596/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951581/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951652/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951695/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951758/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951814/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951883/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53951980/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53952022/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53952056/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53952151/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53952328/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53952850/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53952951/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953009/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953031/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953087/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953296/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953450/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953496/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953622/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953686/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953841/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53953959/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53954127/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53991836/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53992013/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/53992122/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54757610/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54757672/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54757782/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54757873/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54757972/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758296/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758366/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758412/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758493/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758600/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758628/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54758947/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759051/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759105/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759182/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759255/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759344/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759447/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759491/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54759552/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54760559/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54760631/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54760689/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54760778/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54760843/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761007/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761093/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761194/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761285/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761336/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761414/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761474/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761537/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761624/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761689/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761721/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761771/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761788/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761855/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761914/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54761987/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54762080/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54769971/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770098/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770178/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770243/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770412/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770509/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770610/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770638/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770730/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770816/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770866/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770925/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54770983/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771053/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771097/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771264/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771317/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771358/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771443/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771579/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771691/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771765/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771832/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54771946/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54772182/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/54772390/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55045752/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55045858/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55083162/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55083365/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55083443/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55083746/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55083835/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55083888/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55085943/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55085997/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55086036/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55225236/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55225340/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55225442/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55225926/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55226130/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55226165/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55226253/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55226310/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55226383/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55232334/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55232345/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55232473/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55232627/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55233166/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55233434/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55234026/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55235044/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55236552/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55237516/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238361/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238373/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238472/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238518/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238588/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238649/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238682/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238769/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55238892/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55244616/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55245553/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55245938/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55246152/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55249448/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55249521/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55249762/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55282572/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55283040/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55283282/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55283585/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55283912/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55287090/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55287273/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55287475/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55288553/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55289247/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55289440/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55290839/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55291553/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55291726/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55291926/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55292335/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55308576/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55308761/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55308990/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55309125/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55309264/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55309331/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/55309480/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/56047400/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/56047872/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/58089617/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59222767/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59241773/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59242641/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59706179/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/59706221/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60196644/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60284170/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60324430/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60324651/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60327512/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60328219/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60328504/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60328859/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60329038/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60647323/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60647426/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60647529/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60647603/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/60647990/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/61375125/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/61376026/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/62696775/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/62867376/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/62868481/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/64251352/overview', 'https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/64251425/overview']


#code start here



#veriables to track activity in terminal

footer_found = 0
footer_didnt_found = 0
logo_found = 0
logo_didnt_found = 0
seo_found = 0
total = 0
got_it = 0

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
    global got_it
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get('https://infoa9bf3f-app.clickfunnels.com/funnels/8212285/steps/50309042/overview')
    print('login successfully')
    try :
        driver.find_element_by_xpath('//a[contains(text(),"Got it!")]').click()
    except:
        got_it += 1
    sleep(10)


def change_image(link):
    global logo_found
    global logo_didnt_found
    driver.get(link)
    #Click "edit Page"
    sleep(10)
    next_button = find_element_by_xpath("//a[contains(@class,'btn btn-warning openPageInEditor')])[1]")
    driver.execute_script("arguments[0].click()",next_button)

    sleep(9)
    #check if there are any logo
    #b1
    try:
        try:
            #black logo
            logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/04/c9f6a8e0b34daebb44ddbdf3dd7d97/FinalLogoDark_600px_2021.png')]")
            logo.click()
            #click on advance settings
            advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
            advance_settings.click()
            #image input field
            sleep(5)
            img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
            sleep(1)
            img_input.clear()
            sleep(1)
            img_input.send_keys('https://images.clickfunnels.com/8a/39d718264b4782bd5712737494a73b/ConfiLogoBLACK.png')
            #close settings and Save
        
            go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
            # driver.execute_script("arguments[0],click()",go_back)
            # ActionChains(driver).move_by_offset(-70,20).click().perform()
            sleep(1)
            # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
            save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
            driver.execute_script("arguments[0].click()",save__)

            logo_found += 1
        except:
            try:
                #b2
                #black logo
                logo = driver.find_element_by_xpath("//img[contains(@src,https://images.clickfunnels.com/24/c0c405488c4ffba57a8cce8e2e5750/FinalLogoDark.png)]")
                logo.click()
                #click on advance settings
                advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
                advance_settings.click()
                #image input field
                sleep(5)
                img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
                sleep(1)
                img_input.clear()
                sleep(1)
                img_input.send_keys('https://images.clickfunnels.com/8a/39d718264b4782bd5712737494a73b/ConfiLogoBLACK.png')
                #close settings and Save
            
                go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
                # driver.execute_script("arguments[0],click()",go_back)
                # ActionChains(driver).move_by_offset(-70,20).click().perform()
                sleep(1)
                # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
                save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
                driver.execute_script("arguments[0].click()",save__)

                logo_found += 1

            except:
                try:
                    #white logo
                    logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/8a/083c5adb0540b89a761f7b49f12e7f/FinalLogoWhite_600px.png')]")
                    logo.click()
                    #click on advance settings
                    advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
                    advance_settings.click()
                    #image input field
                    sleep(5)
                    img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
                    sleep(1)
                    img_input.clear()
                    sleep(1)
                    img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
                    #close settings and Save
                
                    go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
                    # driver.execute_script("arguments[0],click()",go_back)
                    # ActionChains(driver).move_by_offset(-70,20).click().perform()
                    sleep(1)
                    # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
                    save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
                    driver.execute_script("arguments[0].click()",save__)

                    logo_found += 1
                except:
                    #w2
                    try:
                        #white logo
                        logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/94/7774b1d84a44ea840f760845e5866f/FinalLogoWhite_600px_2021.png')]")
                        logo.click()
                        #click on advance settings
                        advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
                        advance_settings.click()
                        #image input field
                        sleep(5)
                        img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
                        sleep(1)
                        img_input.clear()
                        sleep(1)
                        img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
                        #close settings and Save
                    
                        go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
                        # driver.execute_script("arguments[0],click()",go_back)
                        # ActionChains(driver).move_by_offset(-70,20).click().perform()
                        sleep(1)
                        # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
                        save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
                        driver.execute_script("arguments[0].click()",save__)

                        logo_found += 1

                    except:
                        #w3
                        try:
                            #white logo
                            logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/40/4531a937d54d34ae992a5e2903e15e/FinalLogoWhite_250px.png')]")
                            logo.click()
                            #click on advance settings
                            advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
                            advance_settings.click()
                            #image input field
                            sleep(5)
                            img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
                            sleep(1)
                            img_input.clear()
                            sleep(1)
                            img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
                            #close settings and Save
                        
                            go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
                            # driver.execute_script("arguments[0],click()",go_back)
                            # ActionChains(driver).move_by_offset(-70,20).click().perform()
                            sleep(1)
                            # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
                            save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
                            driver.execute_script("arguments[0].click()",save__)

                            logo_found += 1

                        except:               
                            try:
                                #white logo
                                logo = driver.find_element_by_xpath("//img[contains(@src,'https://images.clickfunnels.com/07/14e3432cd143be9db53277071d205e/FinalLogoWhite.png')]")
                                logo.click()
                                #click on advance settings
                                advance_settings = driver.find_element_by_xpath("//div[contains(@class,'de-rollover-tools ')][not(contains(@style,'display: none'))]/div[contains(@class,'de-rollover-advance')]")
                                advance_settings.click()
                                #image input field
                                sleep(5)
                                img_input = driver.find_element_by_xpath('//div[contains(@class,"elementSettingsConfigContainer eTabs_settings")]/div/div[1]/input')
                                sleep(1)
                                img_input.clear()
                                sleep(1)
                                img_input.send_keys('https://images.clickfunnels.com/e4/a7a4a155df4e12bd06db300fa428dc/ConfiLogoWHITE.png')
                                #close settings and Save
                                    
                                go_back = driver.find_element_by_xpath('/html/body/div[11]').click()
                                # driver.execute_script("arguments[0],click()",go_back)
                                # ActionChains(driver).move_by_offset(-70,20).click().perform()
                                sleep(1)
                                # driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]').click()
                                save__ = driver.find_element_by_xpath('/html/body/div[68]/div[2]/div[2]/div[2]')
                                driver.execute_script("arguments[0].click()",save__)

                                logo_found += 1

                            except:
                                logo_didnt_found += 1
                                
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
    sleep(7)



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
    sleep(7)


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
    get_cookies()
    # login_with_cookies()
    # collect_all_link()
    # print('collected all link')
    for page_link in link_list:
        change_image(page_link)
        # seo_meta_tag()
        # footer_remove_and_add()
        total += 1
        print(page_link)
        print('___________________________________________')
        print('Pages check done =======>  '+ str(total))
        print('Logo added =====> '+str(logo_found)+ '\n' +'Logo checked found  =====> '+str(logo_didnt_found) )


#start here
main()