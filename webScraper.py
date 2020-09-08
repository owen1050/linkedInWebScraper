# import web driver
from selenium import webdriver
import time

username = "owen1050@gmail.com"

#read password from file so its not on github
f = open("password.txt", "r")
password = f.read()
f.close()

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('I:\\Downloads\\chromedriver_win32\\chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/company/audible-inc/people/')

#sometimes it opens main page and nor dirrectly sign in page
try:
    signInButton = driver.find_element_by_class_name('nav__button-secondary')

    signInButton.click()
except:
    pass

#type username
unameBox = driver.find_element_by_id('username')

unameBox.send_keys(username)

#type password
pwBox = driver.find_element_by_id('password')

pwBox.send_keys(password)

#wait for load
time.sleep(2)


#sometimes the sign in button is 3 someimes it 4
try:
    signInXpath = "/html/body/div/main/div[2]/form/div[4]"
    signInButton = driver.find_element_by_xpath(signInXpath)
except:
    signInXpath = "/html/body/div/main/div[2]/form/div[3]"
    signInButton = driver.find_element_by_xpath(signInXpath)
    
signInButton.click()

#wait for load
time.sleep(3)


#loop forever and print each name, when no more names then scroll down
i = 1
while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    isGood = True
    while isGood:
        try:
            i = i + 1
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
