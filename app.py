# site 1https://lista.mercadolivre.com.br/ps5#D[A:playstation%205]
# site 2 https://www.americanas.com.br/busca/ps-5
# site 3 https://www.magazineluiza.com.br/busca/playstation+5/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import os 

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get('https://lista.mercadolivre.com.br/ps5#D[A:playstation%205]')
mercadoLivre = driver.find_elements(By.XPATH,'//div[@class="ui-search-item__group__element ui-search-price__part-without-link shops__items-group-details"]')
preco_mercadoLivre = mercadoLivre[1].text.split(' ')[0] 
with open('precoss.csv', 'w',newline='',encoding='utf-8') as arquivo:
    arquivo.write(f'site,preço{os.linesep}')
    arquivo.write(f'https://lista.mercadolivre.com.br/ps5#D[A:playstation%205],{preco_mercadoLivre}')
    
