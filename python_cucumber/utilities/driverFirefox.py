import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def get_firefox_driver():
    """Initialize Firefox WebDriver with error handling."""
    try:
        service = Service(GeckoDriverManager().install())
        return webdriver.Firefox(service=service)
    except Exception as e:
        print(f"Error initializing Firefox WebDriver: {e}")
        return None
