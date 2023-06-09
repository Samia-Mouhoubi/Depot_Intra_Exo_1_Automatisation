from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

#===================== QUESTION 1 ===================================
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://videotron.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#===================== QUESTION 2 ===================================
images=driver.find_elements(By.TAG_NAME,"img")
print("il y a ", len(images), "images sur le site")

#===================== QUESTION 3 ===================================
i=1
for image in images:
    alt_text = image.get_attribute("alt")
    print("valeur de l'attribut <alt> de l'image ", i ," : ", alt_text)
    i+=1

#===================== QUESTION 4 ===================================
liens=driver.find_elements(By.TAG_NAME,"a")
print("il y a ", len(liens), "liens sur le site")

#===================== QUESTION 5 ===================================
footer=driver.find_element(By.TAG_NAME,"footer")
liens_footer=footer.find_elements(By.TAG_NAME,"a")
print("il y a ", len(liens_footer), "liens dans la section <footer> sur le site")

#===================== QUESTION 6 ===================================
i=1
for lien in liens_footer:
    href_value = lien.get_attribute("href")
    print("valeur de l'attribut <href> du lien :", i ," : ", href_value)
    i += 1


time.sleep(2)
driver.quit()
