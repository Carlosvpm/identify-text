from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

urls = ['url']
search_text = "termo"

try:    
    for url in urls: 
        driver.get(url)    
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