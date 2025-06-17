from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import os
from datetime import datetime


def before_all(context):
    # Get browser from command line or default to chrome
    browser = context.config.userdata.get('browser', 'chrome').lower()
    print(f"\n=== Selected browser: {browser} ===")
    context.browser = browser


def before_scenario(context, scenario):
    try:
        print(f"\nInitializing {context.browser} driver...")

        if context.browser == "chrome":
            context.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install())
            )
        elif context.browser == "firefox":
            context.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install())
            )
        elif context.browser == "edge":
            context.driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install())
            )
        else:
            raise ValueError(f"Unsupported browser: {context.browser}")

        context.driver.maximize_window()
        context.driver.get("https://opensource-demo.orangehrmlive.com")
        print(f"Browser opened: {context.driver.name} {context.driver.capabilities['browserVersion']}")

    except Exception as e:
        print(f"\nERROR: Failed to initialize driver: {e}")
        scenario.skip(reason=f"Browser initialization failed: {e}")


def after_scenario(context, scenario):
    print(f"After scenario: {scenario.name} | status: {scenario.status}")

    if hasattr(context, 'driver') and context.driver:
        if scenario.status == "failed":
            # Define the absolute path to screenshots directory
            screenshot_dir = r"C:\Users\tkinf\python_cucumber\python_cucumber\utilities\screenshots"

            # Create directory if it doesn't exist
            os.makedirs(screenshot_dir, exist_ok=True)

            # Generate clean filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            scenario_name = "".join(
                c if c.isalnum() or c in ("-", "_") else "_"
                for c in scenario.name
            )
            filename = f"FAILED_{scenario_name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshot_dir, filename)

            # Ensure consistent window size for screenshots
            context.driver.set_window_size(1280, 1024)

            # Save screenshot
            context.driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot saved to: {screenshot_path}")

            # Optional: Auto-open the screenshot (Windows)
            if os.name == 'nt':
                os.startfile(screenshot_path)

        # Close browser
        print(f"\nClosing {context.browser} browser...")
        context.driver.quit()
