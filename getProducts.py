from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

gecko_path = './webdriver/geckodriver.exe'

options = webdriver.firefox.options.Options()
options.headless = True
driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
driver.set_window_size(4096, 4096)

 
#url = 'https://www.adidas.com.br/tenis-mulher'
url = 'https://www.adidas.com.br/tenis-homem'
driver.get(url)
wait = WebDriverWait(driver, 30)
driver.implicitly_wait(5)

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/button')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/button').click()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/button[1]/span')))
driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div[2]/button[1]/span').click()


wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'grid-item')))


#items = driver.find_elements(By.XPATH, '//div[@data-grid-id]')

items = driver.find_elements(By.XPATH, '//div[@class="glass-product-card__assets"]')




print('Numero de Items: ' + str(len(items)))

x = 1
for item in items:
    #print(item.get_attribute('innerHTML'))
    print('------------------------------------------------------------')
    print('Product Name : ' + item.find_element(By.XPATH, './/img[@data-auto-id="image"]').get_attribute('title') )
    print('Product Link : ' + item.find_element(By.XPATH, './/a[@data-auto-id="glass-hockeycard-link"]').get_attribute('href'))
    print('Product Image : ' + item.find_element(By.XPATH, './/img[@data-auto-id="image"]').get_attribute('src'))
    print('Product Price: ' + item.find_element(By.XPATH, './/div[@class="gl-price-item notranslate" or @class="gl-price-item gl-price-item--sale notranslate"]').text )
    print('------------------------------------------------------------')



wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/span[2]')))
numeroPaginas = driver.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[3]/span[2]').text

print('Numero de Paginas: ' + numeroPaginas)


