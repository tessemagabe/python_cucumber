from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_chrome_driver():
    """Initialize Chrome WebDriver with error handling."""
    try:
        service = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=service)
    except Exception as e:
        print(f"Error initializing Chrome WebDriver: {e}")
        return None


