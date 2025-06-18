from seleniumpagefactory import PageFactory

class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()





"""
from seleniumpagefactory import PageFactory

class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def initialize_elements(self):
        self.__post_init__()  # <- This safely sets up the locators

"""

"""
from seleniumpagefactory import PageFactory

class BasePage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        super().__init__()

    def initialize_elements(self):
        self.init_elements()
"""