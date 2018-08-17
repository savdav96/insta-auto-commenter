import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class InstaBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.maximize_window()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        webdriver = self.driver

        webdriver.get("https://www.instagram.com/accounts/login")
        time.sleep(2)

        name_form = webdriver.find_element_by_xpath("//input[@name='username']")
        name_form.clear()
        name_form.send_keys(self.username)

        password_form = webdriver.find_element_by_xpath("//input[@name='password']")
        password_form.clear()
        password_form.send_keys(self.password)

        password_form.send_keys(Keys.RETURN)
        time.sleep(2)


    def find_following(self):

        webdriver = self.driver
        webdriver.get("https://www.instagram.com/"+self.username)
        following = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        element = WebDriverWait(webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]")))
        e1 = WebDriverWait(webdriver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/ul/div/li[1]/div/div[1]/div[2]/div[1]/a")))
        #ActionChains(webdriver).move_to_element(element).perform()
        #ActionChains(webdriver).click(e1).perform()
        self.driver.execute_script("arguments[0].focus();", element)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


bot = InstaBot("savoebbasta", "Ignazio96")
bot.login()
bot.find_following()