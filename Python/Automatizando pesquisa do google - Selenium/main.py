from selenium import webdriver
import time


class Google:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://google.com.br'
        self.search_bar = 'q'  # id
        self.btn_search = 'btnK'  # name
        self.btn_lucky = 'btnI'  # name
    
    def navigate(self):
        self.driver.get(self.url)
    
    def search(self, word='None'):
        self.driver.find_element_by_name(self.search_bar).send_keys(word)
        print("click")
        time.sleep(5)
        self.driver.find_element_by_name(self.btn_search).click()
        print("clicado")


ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
g.search('20th century boys - Manga')
