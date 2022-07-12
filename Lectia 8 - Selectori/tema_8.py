from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)


# Test ID
# # 1
# chrome.get('http://automationpractice.com/index.php')
# # <input class="search_query form-control ac_input" type="text" id="search_query_top" name="search_query" placeholder="Search" value="" autocomplete="off"> >
# search_query_top=chrome.find_element(By.ID,'search_query_top')
# search_query_top.send_keys('dress')
# sleep(3)

# # 2
# chrome.get('https://www.phptravels.net/flights')
# # <input class="form-control autocomplete-airport yes" type="search" placeholder="Flying From" name="from" id="autocomplete" value="">
# airport=chrome.find_element(By.ID,'autocomplete')
# sleep(3)
# airport.send_keys('Bucharest')
# sleep(3)
#
# # 3
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# # <input type="text" class="form-control pac-target-input" id="autocomplete" onfocus="geolocate()" placeholder="Enter address" autocomplete="off">
# adress=chrome.find_element(By.ID,'autocomplete')
# sleep(3)
# adress.send_keys('Paris')
# sleep(3)


# Test Link Text
# # 1
# chrome.get('https://the-internet.herokuapp.com/')
# # <a href="/broken_images">Broken Images</a>
# chrome.find_element(By.LINK_TEXT, 'Broken Images').click()
# sleep(3)

# # 2
# chrome.get('https://jules.app/sign-in')
# sleep(4)
# # <a class="jss17 jss18" data-test-id="forgot-password-link" href="/forgot-password">Forgot password?</a>
# chrome.find_element(By.LINK_TEXT, 'Forgot password?').click()
# sleep(3)

# # 3
# chrome.get('http://automationpractice.com/index.php')
# sleep(4)
# # <a href="http://automationpractice.com/index.php?id_category=3&amp;controller=category" title="Women" class="sf-with-ul">Women</a>
# chrome.find_element(By.LINK_TEXT, 'Women').click()
# sleep(3)

# Test Partial Link Text
# # 1
# chrome.get('https://the-internet.herokuapp.com/')
# # <a href="/broken_images">Broken Images</a>
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Brok').click()
# sleep(3)

# # 2
# chrome.get('https://jules.app/sign-in')
# sleep(4)
# # <a class="jss17 jss18" data-test-id="forgot-password-link" href="/forgot-password">Forgot password?</a>
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Forg').click()
# sleep(3)

# # 3
# chrome.get('http://automationpractice.com/index.php')
# sleep(4)
# # <a href="http://automationpractice.com/index.php?id_category=3&amp;controller=category" title="Women" class="sf-with-ul">Women</a>
# chrome.find_element(By.PARTIAL_LINK_TEXT, 'Wom').click()
# sleep(3)

# Test Name
# # 1
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# # <input class="is_required validate account_input form-control" data-validate="isEmail" type="text" id="email" name="email" value="">
# chrome.find_element(By.NAME,'email').send_keys('ioanapopa@gmail.com')
# sleep(3)

# # 2
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# # <input name="firstname" style="-webkit-appearance: none; appearance: none; background-color: #fcfcfc; border-color: rgba(173, 176, 182, 0.3); border-radius: 0px; border-style: solid; border-width: 1px; color: #787d85; font-family: verdana, helvetica, arial, verdana, sans-serif; font-size: 13px; height: 38px; line-height: 22px; margin: 0px; outline: 0px; padding: 5px 15px; vertical-align: baseline;" type="text">
# chrome.find_element(By.NAME,'firstname').send_keys('Stefan')
# sleep(3)

# # 3
# chrome.get('https://the-internet.herokuapp.com/login')
# # <input type="text" name="username" id="username">
# chrome.find_element(By.NAME,'username').send_keys('abramburica')
# sleep(3)

# Test Tag
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(3)
# lista_taguri=chrome.find_elements(By.TAG_NAME,'input')
# print(len(lista_taguri))
# lista_taguri[0].send_keys('Stefan')
# sleep(2)
# lista_taguri[1].send_keys('Popa')
# sleep(2)
# lista_taguri[2].click()
# sleep(3)

# Test Class
# # 1
# chrome.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
# sleep(3)
# lista_clase=chrome.find_elements(By.CLASS_NAME, 'form-group')
# print(len(lista_clase))
# lista_clase[4].click()
# sleep(3)
#
# # 2
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# sleep(3)
# lista_clase=chrome.find_elements(By.CLASS_NAME,'form-control')
# print(len(lista_clase))
# lista_clase[3].send_keys('Blabla')
# sleep(3)

# # 3
# chrome.get('http://automationpractice.com/index.php')
# sleep(3)
# lista_clase=chrome.find_elements(By.CLASS_NAME,'container')
# print(len(lista_clase))
# lista_clase[0].click()
# sleep(3)

# Test CSS
# # 1
# chrome.get('https://jules.app/sign-in')
# sleep(3)
# # <input aria-invalid="false" autocomplete="on" placeholder="Enter your email" type="text" class="MuiInputBase-input MuiFilledInput-input" value="">
# chrome.find_element(By.CSS_SELECTOR,'input[placeholder="Enter your email"]').send_keys('blabla@yahoo.com')
# sleep(3)

# # 2
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(3)
# # <input id="sex-1" name="sex" style="font-size: 14px; margin-left: 0px; margin-right: 0px; margin-top: 0px; padding: 0px; vertical-align: baseline;" type="radio" value="Female">
# chrome.find_element(By.CSS_SELECTOR,'input#sex-1').click()
# sleep(3)

# # 3
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# sleep(3)
# # <input type="text" class="form-control pac-target-input" id="autocomplete" onfocus="geolocate()" placeholder="Enter address" autocomplete="off">
# chrome.find_element(By.CSS_SELECTOR,'input.form-control').send_keys('cucu@gmail.com')
# sleep(3)

# Test XPATH
# chrome.get('http://automationpractice.com/index.php')
# sleep(3)
# # /html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]
# # //*[@id="search_query_top"]
# chrome.find_element(By.XPATH,' //*[@id="search_query_top"]').send_keys('dress')
# sleep(3)


# chrome.get('https://www.phptravels.net/')
# sleep(3)
# # # //*[@id="select2-hotels_city-container"]
# # chrome.find_element(By.XPATH,'//span[@id="select2-hotels_city-container"]').click()
# # sleep(3)
#
# # /html/body/section[6]/div[2]/div/div/div/div/div/a
# chrome.find_element(By.XPATH,'/html/body/section[6]/div[2]/div/div/div/div/div/a').send_keys('i')
# sleep(3)


# chrome.get('https://www.phptravels.net/contact')
# sleep(3)
# # //*[@id="fadein"]/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/input
# # /html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/input
# chrome.find_element(By.XPATH,'/html/body/section[2]/div/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div/input').send_keys('Ana')
# sleep(3)