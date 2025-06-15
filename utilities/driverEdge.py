from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_edge_driver():
    """Initialize Edge WebDriver with error handling."""
    try:
        service = Service(EdgeChromiumDriverManager().install())
        return webdriver.Edge(service=service)
    except Exception as e:
        print(f"Error initializing Edge WebDriver: {e}")
        return None
