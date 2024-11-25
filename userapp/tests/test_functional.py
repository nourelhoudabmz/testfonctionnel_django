from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import os

class TestAjoutProduit:
    def setup_method(self):
        # Initialiser le driver (ici avec Chrome)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def test_ajout_produit(self):
        # Naviguer vers la page
        self.driver.get("http://127.0.0.1:8000/create-product/")
        
        try:
            # Attendre que la page soit chargée
            wait = WebDriverWait(self.driver, 10)
            
            # Remplir le nom du produit
            product_name = wait.until(EC.presence_of_element_located((By.NAME, "product_name")))
            product_name.send_keys("Test Produit Automatisé")
            
            # Gérer l'upload de l'image
            # Assurez-vous que le chemin vers l'image est correct
            image_path = os.path.abspath("chemin/vers/votre/image.jpg")
            file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
            file_input.send_keys(image_path)
            
            # Remplir les tags
            tags_input = self.driver.find_element(By.NAME, "tags")
            tags_input.send_keys("tag1, tag2, tag3")
            
            # Remplir la description
            description = self.driver.find_element(By.NAME, "description")
            description.send_keys("Ceci est une description de test automatisée.")
            
            # Sélectionner la catégorie
            category_select = Select(self.driver.find_element(By.NAME, "category"))
            category_select.select_by_index(1)  # Sélectionne la première option
            
            # Cliquer sur le bouton Add
            add_button = self.driver.find_element(By.CSS_SELECTOR, "button.btn-success")
            add_button.click()
            
            # Attendre un peu pour voir le résultat
            time.sleep(2)
            
            # Vérifier si l'ajout a réussi (à adapter selon votre application)
            # Par exemple, vérifier si on est redirigé vers une page de succès
            assert "success" in self.driver.current_url, "L'ajout du produit a échoué"
            
        except Exception as e:
            print(f"Une erreur s'est produite: {str(e)}")
            raise
        
    def teardown_method(self):
        # Fermer le navigateur
        self.driver.quit()

if __name__ == "__main__":
    # Exécuter le test
    test = TestAjoutProduit()
    try:
        test.setup_method()
        test.test_ajout_produit()
    finally:
        test.teardown_method()