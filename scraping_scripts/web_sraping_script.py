import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrape_site(URL):
    criteria = webdriver.ChromeOptions()
    criteria.headless = True
    criteria.add_argument("window_size=1920x1080")
    criteria.add_argument('--no-sandbox')
    criteria.add_argument('--disable-gpu')
    
    driver = webdriver.Chrome(options=criteria)
    driver.get(URL)

    time.sleep(5)

    element1 = driver.find_element_by_class_name('titlelink').text
    print(element1)

    driver.close()

    return element1


