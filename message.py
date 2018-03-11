import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

class sendMessage:

    def __init__(self):

        #self.display = Display(visible=0, size=(1024, 768))
        #self.display.start()
        self.driver=webdriver.Chrome()
        self.driver.get(url='https://web.whatsapp.com/')
        self.timeout = 100
    def searchChat(self,name):
        #time.sleep(25)
        try:
            element_present = EC.presence_of_element_located((By.ID, 'input-chatlist-search'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            print("Not Connected")
        search= self.driver.find_element_by_id("input-chatlist-search")
        search.send_keys(name + Keys.ENTER)
       # time.sleep(15)
        # clickSearch=self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[1]/span").click()
        #time.sleep(10)
    def sendText(self,message1):
        try:
            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
        except TimeoutException:
            print("Not Connected")

        message=self.driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]")
        message.send_keys(message1 + Keys.ENTER)
        #time.sleep(3)
        #click=self.driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/button").click()
filepath="String.txt"
with open(filepath) as fp:
    name=fp.readline()
    message1=fp.readline()
class_object=sendMessage()
class_object.searchChat(name)
class_object.sendText(message1)


