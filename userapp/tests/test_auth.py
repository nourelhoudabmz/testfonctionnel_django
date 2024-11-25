# Importations communes
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
# Test pour l'inscription
class TestTestregister:
    def setup_method(self, method):
       service = Service(executable_path="C:/webdriver/msedgedriver.exe")
       self.driver = webdriver.Edge(service=service)
       self.vars = {}
       time.sleep(2) 

    def teardown_method(self, method):
        self.driver.quit()

    def test_testregister(self):
        self.driver.get("http://127.0.0.1:8000/signup/")
        time.sleep(2)
        self.driver.set_window_size(1272, 816)
        self.driver.find_element(By.ID, "id_username").send_keys("Nourboumaiza")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_password").send_keys("nour123")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_email").send_keys("nourelhouda.iot@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_first_name").send_keys("nour elhouda")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_last_name").send_keys("boumaiza")
        time.sleep(2)
        self.driver.find_element(By.NAME, "Register").click()

# Test pour la connexion
class TestTestlogin:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testlogin(self):
        self.driver.get("http://127.0.0.1:8000/accounts/login/")
        self.driver.set_window_size(1272, 816)
        self.driver.find_element(By.ID, "id_username").send_keys("Nourboumaiza")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_password").send_keys("nour123")
        time.sleep(2)
        self.driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
