#Libraries
import time

import telebot
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#Variables
bot_token = "5563831970:AAGBSz1vVCvsfi4unwZkRGBVvbW2-Jl5k9k"
mail = "zpbvklae@candassociates.com"
paswd = "Hack@avi1"

#Objects
bot = telebot.TeleBot(bot_token)
browser = webdriver.Chrome('./chromedriver')


#MessageHandling
@bot.message_handler(commands=['login', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Logging In!")
    browser.get("https://dashboard.celltracker.io/login")
    mfield = browser.find_element(By.ID, 'email')
    mfield.click()
    mfield.send_keys(mail)
    time.sleep(3)
    bot.send_message(message.chat.id ,"Entered Mail")

    pfield = browser.find_element(By.ID, 'password')
    pfield.click()
    bot.send_message(message.chat.id ,"Enetred Pass")
    pfield.send_keys(paswd)
    time.sleep(3)

    lbtn = browser.find_element(By.XPATH, '//*[@id="js-login"]/div[5]/div/button')
    lbtn.click()
    bot.send_message(message.chat.id ,"Login Succesfull")
    time.sleep(5)
    dname = browser.find_element(By.XPATH,'//*[@id="device"]/option')

    btry = browser.find_element(By.XPATH, '//*[@id="top"]/div/div/div[3]/div[1]/div/div[3]/div/div[1]/p')
    time.sleep(3)
    status = browser.find_element(By.XPATH, '//*[@id="top"]/div/div/div[3]/div[2]/div/div[3]/div[1]/div[1]/p/span')

    bot.send_message(message.chat.id,'Device Name  =  ' + str(dname.text) + '\n' +'Status              =  ' + str(status.text) + '\n'+ 'Battery             =  ' + str(btry.text))
#

#Work Below

wait = WebDriverWait(browser, 5)

@bot.message_handler(commands=['sms'])
def sms(message):
    browser.find_element(By.XPATH, '// *[ @ id = "sidebarMenu"] / div / ul / li[3] / a / div / span[2]').click()
    time.sleep(2)
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="dismiss-button"]/div/span' ))).click()  #'//*[@id="dismiss-button"]/div/svg'
    except TimeoutException:
        pass













bot.polling()




# print(driver.title)