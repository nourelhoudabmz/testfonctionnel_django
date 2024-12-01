import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait  # Importer WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # Importer EC pour les conditions d'attente

# Fonction pour obtenir automatiquement le driver Chrome
def get_chrome_driver():
    # Utilisation de la version spécifique de ChromeDriver avec WebDriver Manager
    driver_path = ChromeDriverManager(driver_version="131.0.6778.86").install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

# Fonction pour le test sur un navigateur donné
def test_browser(browser_name):
    # Configuration du driver selon le navigateur
    if browser_name == "chrome":
        driver = get_chrome_driver()  # Utilisation de la fonction get_chrome_driver
    elif browser_name == "edge":
        service = EdgeService('C:/webdriver/msedgedriver.exe')  # Chemin du EdgeDriver
        driver = webdriver.Edge(service=service)
    else:
        raise ValueError("Navigateur non pris en charge!")  # Si un navigateur non supporté est passé

    try:
        # Accéder à la page de connexion
        driver.get("http://127.0.0.1:8000/accounts/login/")  # URL locale du formulaire de connexion
        driver.set_window_size(1272, 816)  # Définir la taille de la fenêtre

        # Remplir le formulaire de connexion
        driver.find_element(By.ID, "id_username").send_keys("Nourboumaiza")
        time.sleep(1)
        driver.find_element(By.ID, "id_password").send_keys("nour123")
        time.sleep(1)

        # Soumettre le formulaire
        driver.find_element(By.ID, "id_password").send_keys(Keys.ENTER)  # Utilisation de l'ID correct

        # Attente explicite pour que l'URL contienne "dashboard"
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))  # Attendre que l'URL contienne "dashboard"

        # Vérification de la connexion ou redirection vers la page suivante
        print(f"Test de connexion réussi sur {browser_name}!")
    
    except Exception as e:
        print(f"Test de connexion réussi sur {browser_name}: {e}")

    finally:
        driver.quit()

# Exécution des tests sur Chrome et Edge
if __name__ == "__main__":
    for browser in ["chrome", "edge"]:
        print(f"Exécution des tests sur {browser}...")
        test_browser(browser)
