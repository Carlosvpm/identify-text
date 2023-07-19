from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

urls = ["https://vidav.com.br/", 'https://vidav.com.br/sobre/', 'https://vidav.com.br/rede/', 'https://vidav.com.br/especialidades/nutricionista/', 'https://vidav.com.br/ajuda/', 'https://vidav.com.br/saude-v/']

try:
    
    for url in urls: 
        driver.get(url)
        search_text = "Vida V"
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