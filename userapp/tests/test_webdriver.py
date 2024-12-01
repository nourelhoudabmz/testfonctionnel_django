from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
# Spécifiez le chemin vers votre WebDriver
service = Service("C:/webdriver/msedgedriver.exe")  # Remplacez par le chemin réel de msedgedriver.exe

# Initialisez le WebDriver
driver = webdriver.Edge(service=service)

# Accédez à une URL pour tester
driver.get("https://www.google.com")

print("Test réussi : le navigateur s'est ouvert.")
time.sleep(2)
driver.quit()
