import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from helpersF import *
from fixture import *
from upload_to_testrail import *


# Load all scenarios from the feature file
scenarios("signup.feature")

@pytest.fixture()
def variables():
    return {
        "driver": None,
        "opened_url": ""
    }

# Scenario: Testing for Successful Sign Up

@given("the user is on the signup page")
def step_given_user_on_signup_page(variables):
    driver = getUrlDriver('https://zouk.co.in/account/register')
    variables["driver"] = driver

@when("entered valid user details")
def step_when_enter_valid_user_details(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerfirst_name', 'test')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerlast_name', 'user')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customeremail', 'test@example.com')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerpassword', 'Valid@123')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')

@then("redirected to home page")
def step_then_redirected_to_home_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in', 'Redirection to home page failed.')

# Scenario: Sign Up with wrong password format 

@when("entered wrong password format")
def step_when_enter_wrong_password_format(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerfirst_name', 'alpha')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerlast_name', 'beeta')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customeremail', 'alphab@example.com')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerpassword', '123')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')

@then("Then the user should redirected to signup page")
def redirected_to_signup_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in', 'Redirection to home page failed.')

# Scenario: Sign Up with wrong email format 

@when("entered wrong email format")
def step_when_enter_wrong_email_format(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerfirst_name', 'hehe')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerlast_name', 'hoho')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customeremail', 'heho@example')
    enter_text(variables["driver"], By.ID, 'input-template--22762731569448__main--customerpassword', '123456')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button') 

# Scenario: Testing if only Email is filled

@given("the user is on the login page")
def step_given_user_on_login_page(variables):
    driver = getUrlDriver('https://zouk.co.in/account/login?return_url=%2Faccount')
    variables["driver"] = driver

@when("the user enters valid email id")
def step_when_enter_valid_email(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customeremail', 'test@example.com')

@when("the user clicks on the login button")
def step_when_user_clicks_login_button(variables):
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/account-login/div[1]/div[3]/form/button')

@then("the user should redirected to home page")
def redirected_to_login_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in/account/login?return_url=%2Faccount', 'Redirection to home page failed.')

# Scenario: Testing if only password is filled

@when("the user enters valid password")
def step_when_enter_valid_password(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customerpassword', 'ValidPassword123')

# Scenario: Successful login with valid credentials

@when("the user enters valid credentials")
def step_when_enter_valid_credentials(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customeremail', 'manna2024@gmail.com')
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customerpassword', 'manna@2024')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')

@then("the user should be redirected to the dashboard")
def step_then_redirected_to_dashboard(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in/account', 'Redirection to dashboard failed.')

# Scenario: Unsuccessful login with invalid credentials

@when("the user enters invalid credentials")
def step_when_enter_invalid_credentials(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customeremail', 'baba2024@gmail.com')
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customerpassword', 'baba@2024')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')

# Scenario: Unsuccessful login with empty fields

@when("the user leaves the username and password fields empty")
def empty_credentials(variables):
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customeremail', '')
    enter_text(variables["driver"], By.ID, 'input-template--22965915648296__main--customerpassword', '')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')
    
# Scenario: Testing for forget password

@when("the user clicks on the forget password button")  
def forget_password(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/account-login/div[1]/div[3]/form/div[1]/div[2]/div[2]/a')
   
   
@then("the user should redirected to recover your password page")
def recover_your_password_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in/account/login?return_url=%2Faccount#recover', 'Redirection to dashboard failed.')
    
    
# Scenario: Testing if mandatory fields are  not filled    
    