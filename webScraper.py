# import web driver
from selenium import webdriver
import time

username = "owen1050@gmail.com"
password = ""

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('I:\\Downloads\\chromedriver_win32\\chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/company/audible-inc/people/')

# locate email form by_class_name
try:
    signInButton = driver.find_element_by_class_name('nav__button-secondary')

    signInButton.click()
except:
    pass

unameBox = driver.find_element_by_id('username')

unameBox.send_keys(username)

pwBox = driver.find_element_by_id('password')

pwBox.send_keys(password)

time.sleep(2)

try:
    signInXpath = "/html/body/div/main/div[2]/form/div[4]"
    signInButton = driver.find_element_by_xpath(signInXpath)
except:
    signInXpath = "/html/body/div/main/div[2]/form/div[3]"
    signInButton = driver.find_element_by_xpath(signInXpath)
    
signInButton.click()


time.sleep(3)

i = 1
while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    isGood = True
    while isGood:
        try:
            i = i + 1
            print(i)
            #        /html/body/div[7]/div[3]/div/div[3]/div[2]/div[2]/div[2]/ul/li[997]        /div/section/div/div/div[2]/div[1]/a/div
            nameX = "/html/body/div[7]/div[3]/div/div[3]/div[2]/div[2]/div[2]/ul/li["+ str(i)+"]/div/section/div/div/div[2]/div[1]/a/div"
            name = driver.find_element_by_xpath(nameX)
            nameText = str(name.text)
            print(nameText)
            if nameText == "":
                pass
            else:
                pass
                #print(i, nameText)
            
            
        except:
            isGood = False

# send_keys() to simulate key strokes
#username.send_keys('example@gmail.com')
#/html/body/div[7]/div[3]/div/div[3]/div[2]/div[2]/div[2]/ul/li[997]/div/section/div/div/div[2]/div[1]/a/div