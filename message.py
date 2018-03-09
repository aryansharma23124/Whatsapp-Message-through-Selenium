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
    def searchChat(self):
        time.sleep(25)
        search= self.driver.find_element_by_id("input-chatlist-search")
        search.send_keys("anmol" + Keys.ENTER)
        time.sleep(15)
        # clickSearch=self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[1]/span").click()
        time.sleep(10)
        message=self.driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/div[2]/div/div[2]")
        message.send_keys("anmol" + Keys.ENTER)
        # time.sleep(5)
        # click=self.driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/footer/div[1]/button").click()
class_object=sendMessage()
class_object.searchChat()


