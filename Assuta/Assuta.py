from selenium import webdriver


class Assuta:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.mouse = webdriver.ActionChains(self.driver)
