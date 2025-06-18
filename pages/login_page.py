from pages.base_page import BasePage
class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.locator = {
            "username_input": ("NAME", "username"),
            "password_input": ("NAME", "password"),
            "login_button": ("XPATH", "//button[@type='submit']"),
            "error_message": ("CSS", ".oxd-alert-content-text"),
            "dashboard_title": ("XPATH", "//h6[text()='Dashboard']"),
        }
        super().__init__(driver)
        #self.initialize_elements()


"""
from pages.base_page import BasePage  # ✅ Make sure path is correct

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.initialize_elements()  # ✅ Safe call now via BasePage

    locators = {
        "username_input": ("NAME", "username"),
        "password_input": ("NAME", "password"),
        "login_button": ("XPATH", "//button[@type='submit']"),
        "error_message": ("CSS", ".oxd-alert-content-text"),
        "dashboard_title": ("XPATH", "//h6[text()='Dashboard']"),
    }

    def perform_login(self, username, password):
        self.username_input.clear()
        self.username_input.send_keys(username)
        self.password_input.clear()
        self.password_input.send_keys(password)
        self.login_button.click()

    def is_on_dashboard(self):
        return self.dashboard_title.is_displayed()

    def get_error_text(self):
        return self.error_message.text

"""


"""
from seleniumpagefactory import PageFactory

class LoginPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10  # Optional default wait time
        self.init_elements()

    locators = {
        "username_input": ("NAME", "username"),
        "password_input": ("NAME", "password"),
        "login_button": ("XPATH", "//button[@type='submit']"),
        "error_message": ("CSS", ".oxd-alert-content-text"),
        "dashboard_title": ("XPATH", "//h6[text()='Dashboard']"),
    }

    def perform_login(self, username, password):
        self.username_input.clear()
        self.username_input.send_keys(username)
        self.password_input.clear()
        self.password_input.send_keys(password)
        self.login_button.click()

    def is_on_dashboard(self):
        return self.dashboard_title.is_displayed()

    def get_error_text(self):
        return self.error_message.text
"""