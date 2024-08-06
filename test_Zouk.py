import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from helpersF import *
from fixture import *
from xpath import *


# Load all scenarios from the feature file
scenarios("signup.feature")

@pytest.fixture()
def variables():
    return {
        "driver": None,
        "opened_url": ""
    }
    
     
# common steps
@given("the user is on the signup page")
def step_given_user_on_signup_page(variables):
    driver = getUrlDriver(signup_url)
    variables["driver"] = driver


@given("the user is on the login page")
def step_given_user_on_login_page(variables):
    driver = getUrlDriver(login_url)
    variables["driver"] = driver     
    
@when("the user clicks on the login button")
def step_when_user_clicks_login_button(variables):
    click_button(variables["driver"], By.XPATH, login_button)  
    
@then("the user should redirected to home page")
def redirected_to_login_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in/account/login?return_url=%2Faccount', 'Redirection to home page failed.') 
    
@then("the user should be redirected to the dashboard")
def step_then_redirected_to_dashboard(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], '', 'Redirection to dashboard failed.')
    
    

# Scenario: Successful Sign Up
@when("entered valid user details")
def step_when_enter_valid_user_details(variables):
    enter_text(variables["driver"], By.ID, first_name, 'test')
    enter_text(variables["driver"], By.ID, last_name, 'user')
    enter_text(variables["driver"], By.ID, signup_email, 'test@example.com')
    enter_text(variables["driver"], By.ID, s_password, 'Valid@123')
    click_button(variables["driver"], By.XPATH, click)
    
@then("redirected to home page")
def step_then_redirected_to_home_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], z_page , 'Redirection to home page failed.')    
  
  
         
# Scenario: Sign Up with Incorrect Password Format         
@when("entered wrong password format")
def step_when_enter_wrong_password_format(variables):
    enter_text(variables["driver"], By.ID, first_name, 'alpha')
    enter_text(variables["driver"], By.ID, last_name, 'beta')
    enter_text(variables["driver"], By.ID, signup_email, 'alphab@example.com')
    enter_text(variables["driver"], By.ID, s_password , '123')
    click_button(variables["driver"], By.XPATH, click)
         
         
@then("Then the user should redirected to signup page")
def redirected_to_signup_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], z_page, 'Redirection to home page failed.')         
    
    

# Scenario: Sign Up with Incorrect Email Format
@when("entered wrong email format")
def step_when_enter_wrong_email_format(variables):
    enter_text(variables["driver"], By.ID,first_name, 'hehe')
    enter_text(variables["driver"], By.ID, last_name, 'hoho')
    enter_text(variables["driver"], By.ID, signup_email, 'heho@example')
    enter_text(variables["driver"], By.ID, s_password, '123456')
    click_button(variables["driver"], By.XPATH, click)     
 
    
# Scenario: Successful Login with Valid Credentials    
@when("the user enters valid credentials")
def step_when_enter_valid_credentials(variables):
    enter_text(variables["driver"], By.ID, login_id, 'manna2024@gmail.com')
    enter_text(variables["driver"], By.ID, login_password, 'manna@2024')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')
    
 
# Scenario: Testing if only Email is filled
@when("the user enters valid email id")
def step_when_enter_valid_email(variables):
    enter_text(variables["driver"], By.ID, login_id , 'test@example.com')    
    
    
# Scenario: Testing if only password is filled

@when("the user enters valid password")
def step_when_enter_valid_password(variables):
    enter_text(variables["driver"], By.ID, login_password, 'ValidPassword123') 
    
# Scenario: Unsuccessful login with invalid credentials
@when("the user enters invalid credentials")
def step_when_enter_invalid_credentials(variables):
    enter_text(variables["driver"], By.ID, login_id, 'baba2024@gmail.com')
    enter_text(variables["driver"], By.ID, login_password, 'baba@2024')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')      
    
# Scenario: Unsuccessful login with empty fields
@when("the user leaves the username and password fields empty")
def empty_credentials(variables):
    enter_text(variables["driver"], By.ID, login_id , '')
    enter_text(variables["driver"], By.ID,login_password , '')
    click_button(variables["driver"], By.XPATH, '/html/body/main/section/div/div/div/div/div[3]/form/button')    
    
# Scenario: Testing for forget password
@when("the user clicks on the forget password button")  
def forget_password(variables):
  click_button(variables["driver"], By.XPATH, click_forget_password)    
  
  
@then("the user should redirected to recover your password page")
def recover_your_password_page(variables):
    sleep(3)  
    assert_url(variables["driver"], recover_password , 'Redirection to dashboard failed.')  
 
    
# Scenario: bag page    
@when("the user clicks on bag button")
def click_bag_button(variables):
  click_button(variables["driver"], By.XPATH, bag_button)
  
@then("the user should redirected to bag page")  
def redirected_to_bag_page(variables):
    sleep(3) 
    assert_url(variables["driver"], bag_page, 'Redirection to dashboard failed.') 
  

@when("the user is on bag page")
def step_given_user_on_login_page(variables):
    sleep(3)
    driver = getUrlDriver(bag_page)
    variables["driver"] = driver       

@when("the user clicks on bag page filter")
def click_bag_filter(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, bag_filter)    
  
@when("the user clicks on view result")  
def click_view_result(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, view_result)
    
@when("clicks on sort button")
def click_button_sort(variables):
  click_button(variables["driver"], By.XPATH, sort_button)    
  
# Scenario: user selects filter

@when("the user clicks on price tab")  
def click_priceTab(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, price_tab)
  
@when("the user clicks on Product type tab")
def click_product_type_Tab(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, product_tab)     
  
@when("the user clicks on Pattern tab")
def click_pattern_type_Tab(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, pattern_tab)  

@when("the user clicks on Occasion tab")
def click_Occasion_type_Tab(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, occation_tab)  
  
@when("the user clicks on Category tab")
def click_Category_type_Tab(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, category_tab)
  
@when("the user clicks on Color tab")
def click_Color_type_Tab(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, color_tab)    
  
  
# Scenario: user selects from filter

@when("the user selects price")
def select_price(variables):
 sleep(3)
 enter_text(variables["driver"], By.XPATH,price1, '500')
 enter_text(variables["driver"], By.XPATH,price2, '2000')

@when("the user selects Product type")  
def click_product_type(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, product)
  
@when("the user selects Pattern type")  
def click_Pattern_type(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, pattern) 
  
@when("the user selects Occasion type")  
def click_Occasion_type(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, occation) 
  
@when("the user selects Category type")  
def click_Category_type(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, category)    

@when("the user selects Color type") 
def click_Color_type(variables):
  sleep(3)
  click_button(variables["driver"], By.XPATH, color)    
      
      

# Scenario: Products are listed
@then("the bags according to price range are listed") 
def priceRange_bags_listed(variables):
    sleep(3)
    get_element_text(variables["driver"], By.XPATH, price_products)
      
      
@then("the bags according to product type are listed")  
def productType_bags_listed(variables):
    sleep(3)
    get_element_text(variables["driver"], By.XPATH, products_products)

@then("the bags according to Pattern are listed")  
def Pattern_Type_bags_listed(variables):
    sleep(3)
    get_element_text(variables["driver"], By.XPATH, pattern_products)  


@then("the bags according to Occasion are listed")  
def Occasion_Type_bags_listed(variables):
    sleep(3)
    get_element_text(variables["driver"], By.XPATH, occation_products)   

@then("the bags according to Category are listed")  
def Category_Type_bags_listed(variables):
    sleep(3) 
    get_element_text(variables["driver"], By.XPATH, category_products)  

@then("the bags according to Color are listed")  
def Color_Type_bags_listed(variables):
    sleep(3) 
    get_element_text(variables["driver"], By.XPATH, color_products)  
      
      
# Scenario: checking for clear tab    

@when("the user clicks on clear tab")
def click_clear_Tab(variables):
  click_button(variables["driver"], By.XPATH, clear_tab)


# Scenario: Adding product to wishlist

@when("user adds product to wishlist")
def product_whislisted(variables):
  click_button(variables["driver"], By.XPATH, add_wishlist)
  
  
@when("user clicks on wishlist tab")
def product_whislist(variables):
  click_button(variables["driver"], By.XPATH, wishlist_tab)
  
@then("product is added in wishlist")  
def product_whislisted_added(variables):
    get_element_text(variables["driver"], By.XPATH, wishlisted)
    
# Scenario: deleting product from wishlist    

@when("click on remove all from wishlist")
def remove_product(variables):
  click_button(variables["driver"], By.XPATH, remove_wishlist)
  
@when("click on OK")
def click_ok(variables):
  click_button(variables["driver"], By.XPATH, ok_click) 
  
@then("wishlist must be empty")  
def wishlist_empty(variables):
    get_element_text(variables["driver"], By.XPATH, empty_wishlist) 
    
# Scenario: Adding product to cart    

@when("user adds product to cart")
def add_product_cart(variables):
  click_button(variables["driver"], By.XPATH, cart_product)
  
@then("product is added to cart")
def product_added(variables):
    get_element_text(variables["driver"], By.XPATH, cart)


# Scenario: delete product from cart
    
@when("click on remove from cart")
def remove_product_cart(variables):
  click_button(variables["driver"], By.XPATH, remove_cart)
  
@then("Now cart is empty")  
def empty_cart(variables):
    get_element_text(variables["driver"], By.XPATH, empty_cart)         
# Scenario: sorting products
@when("selects sort Alphabetically A-Z")
def click_button_Alphabetically1(variables):
  click_button(variables["driver"], By.XPATH, Alphabetically_sort)
  
@when("selects sort Price-low to high")
def click_button_Price_low2high(variables):
  click_button(variables["driver"], By.XPATH, price_sort)

@when("selects sort Date-old to new")
def click_button_old2new(variables):
  click_button(variables["driver"], By.XPATH, date_sort)
  
# Scenario: sorted products listed
@then("Products are Alphabetically sorted")  
def Alphabetically_sorted(variables):
    get_element_text(variables["driver"], By.XPATH, alp_products)

@then("Products are Price-low to high sorted")  
def price_sorted_low2high(variables):
    get_element_text(variables["driver"], By.XPATH, low)   
      
@then("Products are Date-old to new sorted")  
def price_sorted_old2new(variables):
    get_element_text(variables["driver"], By.XPATH, old)          
  
  
      