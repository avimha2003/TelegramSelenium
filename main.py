#Libraries
import time

import telebot
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

op = Options()
op.add_extension('AdBlock-—-best-ad-blocker.crx')

#Variables
bot_token = "5563831970:AAGBSz1vVCvsfi4unwZkRGBVvbW2-Jl5k9k"
mail = "zpbvklae@candassociates.com"
paswd = "Hack@avi1"

#Objects
bot = telebot.TeleBot(bot_token)
browser = webdriver.Chrome('./chromedriver',options=op)
time.sleep(5)
browser.switch_to.window(browser.window_handles[1])
browser.close()


#MessageHandling
@bot.message_handler(commands=['login', 'help'])
def send_welcome(message):

    browser.switch_to.window(browser.window_handles[0])

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

#SmS
@bot.message_handler(commands=['sms'])
def sms(message):
    browser.find_element(By.XPATH, '// *[ @ id = "sidebarMenu"] / div / ul / li[3] / a / div / span[2]').click()
    bot.send_message(message.chat.id, "Clicked SmS")

#CallsLogs
@bot.message_handler(commands=['callslogs'])
def calls(message):
    browser.find_element(By.XPATH, '//*[@id="sidebarMenu"]/div/ul/li[4]/a/div/span[2]').click()
    bot.send_message(message.chat.id, "Clicked callslogs")


#CallRec
@bot.message_handler(commands=['callrec'])
def callrec(message):
    browser.find_element(By.XPATH, '//*[@id="sidebarMenu"]/div/ul/li[5]/a/div/span[2]').click()
    bot.send_message(message.chat.id, "Clicked callrec")

#Location
@bot.message_handler(commands=['location'])
def location(message):
    browser.find_element(By.XPATH, '//*[@id="sidebarMenu"]/div/ul/li[6]/a/div/span[2]').click()
    bot.send_message(message.chat.id, "Clicked location")


 #Contacts
@bot.message_handler(commands=['contacts'])
def Contacts(message):
    browser.find_element(By.XPATH, '//*[@id="sidebarMenu"]/div/ul/li[7]/a/div').click()
    bot.send_message(message.chat.id, "Clicked Contacts")

 #WhatsApp
@bot.message_handler(commands=['whatsapp'])
def whatsapp(message):
    browser.find_element(By.XPATH, '//*[@id="sidebarMenu"]/div/ul/li[8]/a').click()
    bot.send_message(message.chat.id, "Clicked WhatsApp")


@bot.message_handler(commands=['exit'])
def exit(message):
    browser.close()














bot.polling()




# print(driver.title)