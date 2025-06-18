from behave import given, when, then
from pages.login_page import LoginPage  # Adjust if the path is different

@given("the user is on the OrangeHRM login page")
def step_given_login_page(context):
    context.login_page = LoginPage(context.driver)
    # No need to manually initialize elements—PageFactory handles this internally

@when('the user enters username "{username}" and password "{password}"')
def step_when_enter_credentials(context, username, password):
    context.login_page.perform_login(username, password)

@then("the user should be redirected to the dashboard")
def step_then_redirect_dashboard(context):
    # Force failure for screenshot testing
    assert "NOT_DASHBOARD" in context.login_page.dashboard_title.text, \
        "Forced failure to test screenshot"

@then('the user should see an error message "{error_message}"')
def step_then_see_error(context, error_message):
    actual_error = context.login_page.get_error_text()
    assert error_message in actual_error, f"Expected error '{error_message}', got '{actual_error}'"





"""
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("the user is on the OrangeHRM login page")
def step_given_login_page(context):
    # No need to initialize WebDriver here (already handled in setup)
    pass


@when('the user enters username "{username}" and password "{password}"')
def step_when_enter_credentials(context, username, password):
    wait = WebDriverWait(context.driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))

    username_field.clear()
    username_field.send_keys(username)
    password_field.clear()
    password_field.send_keys(password)

    login_button = context.driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

""" """
@then("the user should be redirected to the dashboard")
def step_then_redirect_dashboard(context):
    wait = WebDriverWait(context.driver, 10)
    dashboard_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))
    assert dashboard_header.is_displayed(), "Dashboard header not displayed"
""""""
# the above code is the right code and would not fail
# the one below is made to fail for screenshot purpose

@then("the user should be redirected to the dashboard")
def step_then_redirect_dashboard(context):
    wait = WebDriverWait(context.driver, 10)
    dashboard_header = wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    # Force a failure here:
    assert "NOT_DASHBOARD" in dashboard_header.text, "Forced failure to test screenshot"


@then('the user should see an error message "{error_message}"')
def step_then_see_error(context, error_message):
    wait = WebDriverWait(context.driver, 10)
    error_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-alert-content-text")))

    actual_error = error_element.text
    assert error_message in actual_error, f"Expected error '{error_message}', got '{actual_error}'"

"""

