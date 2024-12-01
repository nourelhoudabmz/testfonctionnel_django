import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestTestupdate():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}
    
    def teardown_method(self, method):
        self.driver.quit()
    
    def test_testupdate(self):
        self.driver.get("http://127.0.0.1:8000/update-product/14")
        self.driver.set_window_size(1280, 816)
        
        # Attendre que les champs soient chargés
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_product_name"))
        )
        
        # Réinitialiser les champs
        self.driver.find_element(By.ID, "id_product_name").clear()
        self.driver.find_element(By.ID, "id_description").clear()
        
        # Ajouter de nouvelles valeurs
        self.driver.find_element(By.ID, "id_product_name").send_keys("iphone 15 Pro Max")
        
        self.driver.find_element(By.ID, "id_image").send_keys("C:\\Users\\nourn\\OneDrive\\Images\\iphone-15-pro.jpg")
        
        # Réinitialiser les tags avant de sélectionner de nouveaux
        dropdown = self.driver.find_element(By.ID, "id_tags")
        dropdown.find_element(By.XPATH, "//option[. = 'Smartphone']").click()
        dropdown.find_element(By.XPATH, "//option[. = 'Laptop']").click()
        
        # Description
        self.driver.find_element(By.ID, "id_description").send_keys(
            "Écran Super Retina XDR, Puce A17 Pro, Caméra avancée."
        )
        
        # Sélectionner une nouvelle catégorie
        dropdown = self.driver.find_element(By.ID, "id_category")
        dropdown.find_element(By.XPATH, "//option[. = 'Electronics']").click()
        
        # Soumettre le formulaire
        self.driver.find_element(By.NAME, "button").click()
