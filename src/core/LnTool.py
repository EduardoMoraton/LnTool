from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import os

import pickle
from time import sleep

from pathlib import Path
import requests

OWN_PATH = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div[1]/a"
IMG_PATH = "/html/body/div[5]/div[3]/div/div/div[2]/div/div/div/div/div[1]/div[1]/a/div[1]/img"

class LnTool:
    def __init__(self, driver_path, cookies_path):
        self.driver_path = driver_path
        self.cookies_path = cookies_path
        self.current_session = None
        self.driver = webdriver.Chrome(executable_path=driver_path)
    
    def start(self):
        self.driver.get("https://www.google.es")
    
    @property
    def sesions(self) -> list:
        return [os.path.join(self.cookies_path, f) for f in os.listdir(self.cookies_path) if os.path.isfile(os.path.join(self.cookies_path, f))]
    
    def current_session_avatar(self) -> str:
        wait = WebDriverWait(self.driver, 500)
        condition = EC.presence_of_element_located((By.XPATH, IMG_PATH))
        wait.until(condition)
        return  self.driver.find_element(By.XPATH, IMG_PATH).get_attribute("src")
    
    def set_session(self, index):
        self.current_session = self.sesions[index]

    def load_session(self):
        self.driver.get("https://www.linkedin.com/")
        cookies = pickle.load(open(self.current_session, "rb"))
        for cookie in cookies:
            print(cookie)
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        
    def create_session(self, session_name):
        LN_BAR_ME = "/html/body/div[6]/header/div/nav/ul/li[6]"
        self.driver.get("https://www.linkedin.com/login/")
        wait = WebDriverWait(self.driver, 500)


        condition = EC.presence_of_element_located((By.XPATH, LN_BAR_ME))
        wait.until(condition)

        pickle.dump(self.driver.get_cookies(), open(self.cookies_path+session_name+"", "wb"))
    
    
    def load_works(self, name, location, pages = 1):
        WORK_TAB = "/html/body/div[6]/header/div/nav/ul/li[3]/a"
        SEARCH_BAR = "/html/body/div[6]/header/div/div/div"
        NAME_INPUT = "/html/body/div[6]/header/div/div/div/div[2]/div[2]/div/div[2]/input[1]"
        LOCATION_INPUT = "/html/body/div[6]/header/div/div/div/div[2]/div[3]/div/div/input[1]"
        
        JOB_LIST = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[1]/div/ul"
        JOB_DETAILS = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div"
        
        JOB_DETAILS_NAME = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[1]/a/h2"
        JOB_DETAILS_SHARE_BUTTON = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/button"
        JOB_DETAILS_SHARE_DROPDOWN = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[1]/div/div"
        
        PAGE_LIST = "/html/body/div[6]/div[3]/div[4]/div/div/main/div/div[1]/div/div[7]/ul"
        
        self.find_when_exists(WORK_TAB).click()
        self.find_when_exists(SEARCH_BAR, sleep_time=2).click()
        name_input = self.find_when_exists(NAME_INPUT)
        name_input.send_keys(name)
        self.find_when_exists(LOCATION_INPUT, sleep_time=1).click()
        self.find_when_exists(LOCATION_INPUT).send_keys(location)
        name_input.click()
        name_input.send_keys(Keys.ENTER)
        sleep(5)
        job_list_li = self.find_when_exists(JOB_LIST).find_elements(By.TAG_NAME, "li")
        
        print(len(job_list_li))
        
        for li in job_list_li:
            ActionChains(self.driver).scroll_to_element(li).perform()
            li.click()
            details = self.find_when_exists(JOB_DETAILS)
            print(details.text)
            sleep(1)
        
        
        works = []

    
    def find_when_exists(self, xpath, sleep_time = 0.1) -> WebElement:
        wait = WebDriverWait(self.driver, 500)
        condition = EC.presence_of_element_located((By.XPATH, xpath))
        
        wait.until(condition)
        print("found")
        sleep(sleep_time)
        return self.driver.find_element(By.XPATH, xpath)
    
    def close(self):
        self.driver.close()
        

