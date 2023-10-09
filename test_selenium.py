# abrir a pagina
#
#
#
#

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# service vai executar o chromeDriver manager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# options para mander o navegador aberto
options = webdriver.ChromeOptions()
options .add_experimental_option('detach', True)

# executa o browser com a versao mais recente do chromedriver usando as variavel options para manter o navegador aberto
navegador = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install()))

navegador.get(
    "https://pt.aliexpress.com/?spm=a2g0o.productlist.1000002.1.610ffLRAfLRAU1&gatewayAdapt=glo2bra")
navegador.find_element(
    By.XPATH, '//*[@id="home-firstscreen"]/div/div/div[2]/div/div/div[2]/dl[5]/dt/span/a').click()
navegador.find_element(By.XPATH, '//*[@id="search-key"]').click()
navegador.find_element(
    By.XPATH, '//*[@id="search-key"]').send_keys('tampa xiaomi mi9')
navegador.find_element(
    By.XPATH, '//*[@id="form-searchbar"]/div[1]/input').click()
