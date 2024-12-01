# Generated by Selenium IDE
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddProduct:
    def setup_method(self, method):
        service = Service(executable_path="C:/webdriver/msedgedriver.exe")
        self.driver = webdriver.Edge(service=service)
        self.driver.implicitly_wait(10)  # Implicit wait for elements
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_add_product(self):
        # Accéder à la page de création de produit
        self.driver.get("http://127.0.0.1:8000/create-product/")
        self.driver.set_window_size(1272, 816)

        # 1. Remplir le champ "Nom du produit"
        product_name_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_product_name"))
        )
        product_name_field.click()
        product_name_field.send_keys("MacBook Air M2")
        time.sleep(2) 
        # 2. Ajouter une image
        image_field = self.driver.find_element(By.ID, "id_image")
        image_field.send_keys("C:\\Users\\nourn\\OneDrive\\Images\\mac-book.webp")  # Remplacez par un chemin valide
        time.sleep(2) 
        # 3. Sélectionner une étiquette (tag)
        tags_dropdown = self.driver.find_element(By.ID, "id_tags")
        tags_option = tags_dropdown.find_element(By.XPATH, "//option[. = 'Laptop']")
        tags_option.click()
        time.sleep(2) 
        # 4. Ajouter une description
        description_field = self.driver.find_element(By.ID, "id_description")
        description_field.click()
        description_field.send_keys("Écran 13.6 Liquid Retina LED IPS (2 560 x 1 664 pixels) - Processeur: Apple M2 (CPU 8 coeurs / GPU 8 coeurs / Neural Engine 16 coeurs) - Système d'exploitation: MacOS - Mémoire RAM: 8 Go - Disque Dur: 256 Go SSD avec Wi-Fi, Bluetooth, 2x Thunderbolt/USB 4, Prise casque 3,5 mm, Port de charge MagSafe 3 - Capteur Touch ID, Magic Keyboard rétroéclairé - Couleur: Silver - Garantie: 1 an.")
        time.sleep(2)  
        # 5. Sélectionner une catégorie
        category_dropdown = self.driver.find_element(By.ID, "id_category")
        category_option = category_dropdown.find_element(By.XPATH, "//option[. = 'Computers']")
        category_option.click()
        time.sleep(2) 
        # 6. Soumettre le formulaire
        submit_button = self.driver.find_element(By.NAME, "button")
        submit_button.click()
        time.sleep(2) 
        # 7. Vérification après soumission (par exemple, redirection ou message de succès)
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("all-product")  # Vérifiez si la redirection fonctionne
        )
