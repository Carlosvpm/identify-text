from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


# Adicione as urls que deseja buscar
urls = ['url', 'url']

# Substitua o aqui o texto que deseja buscar
search_text = "termo"

try:    
    for url in urls: 
        driver.get(url)    
        time.sleep(10)    
        text_elements = driver.find_elements("xpath", "//*[contains(text(), '" + search_text + "')]")

        count = 0
        for element in text_elements:
            if element.is_displayed():
                count += 1    

        print(f"O texto '{search_text}' foi encontrado {count} vezes na página: {url}.")

    
except Exception as e:
    print("Termo não encontrado:", e)
finally:
    driver.quit()