import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
from helpersF import *
from fixture import *



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


# Scenario: Check if the clicking on the bag button opens the bag option    

@when("the user clicks on bag button")
def click_bag_button(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/header/height-observer/x-header/nav[1]/ul/li[1]/details/summary')
  
@then("the user should redirected to bag page")  
def redirected_to_bag_page(variables):
    sleep(3)  # Wait for redirection
    assert_url(variables["driver"], 'https://zouk.co.in/collections/bags?ref=nav-top', 'Redirection to dashboard failed.')
    
    
# Scenarios: Selecting bags according to price range from bag filter

@when("the user is on bag page")
def step_given_user_on_login_page(variables):
    sleep(3)  # Wait for redirection
    driver = getUrlDriver('https://zouk.co.in/collections/bags?ref=nav-top')
    variables["driver"] = driver

@when("the user clicks on bag page filter")
def click_bag_filter(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[2]/summary/span/span')
  
@when("the user clicks on price tab")  
def click_priceTab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[2]/summary/span')
  
@when("the user selects price")
def select_price(variables):
 enter_text(variables["driver"], By.XPATH,'/html/body/facets-drawer/form/div/details[2]/div/price-range/div[2]/label[1]/input', '500')
 enter_text(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[2]/div/price-range/div[2]/label[2]/input', '2000')

@when("the user clicks on view result")  
def click_view_result(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/div/button')
  
@then("the bags according to price range are listed") 
def priceRange_bags_listed(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/div[2]/span')


# Scenario: Selecting bags according to Product type    


@when("the user clicks on Product type tab")
def click_product_type_Tab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[3]/summary/span')
  
@when("the user selects Product type")  
def click_product_type(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[3]/div/div/label[1]')
  
@then("the bags according to product type are listed")  
def productType_bags_listed(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/div[3]/span')
    
 
# Scenario: Selecting bags according to Pattern    

@when("the user clicks on Pattern tab")
def click_pattern_type_Tab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[6]/summary/span/span')
  
@when("the user selects Pattern type")  
def click_Pattern_type(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[6]/div/div/label[1]')  
  
@then("the bags according to Pattern are listed")  
def Pattern_Type_bags_listed(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/div[4]/span')  
  

# Scenario: Selecting bags according to Occasion  

@when("the user clicks on Occasion tab")
def click_Occasion_type_Tab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[8]/summary/span/span')
  
@when("the user selects Occasion type")  
def click_Occasion_type(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[8]/div/div/label')    
  
@then("the bags according to Occasion are listed")  
def Occasion_Type_bags_listed(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/div[5]/span')   
    
    
# Scenario: Selecting bags according to Category
    
@when("the user clicks on Category tab")
def click_Category_type_Tab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[4]/summary/span/span')
  
@when("the user selects Category type")  
def click_Category_type(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[4]/div/div/label')    
  
@then("the bags according to Category are listed")  
def Category_Type_bags_listed(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/div[4]/span')  

# Scenario: Selecting bags according to Color
    
@when("the user clicks on Color tab")
def click_Color_type_Tab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[5]/summary/span/span')
  
@when("the user selects Color type") 
def click_Color_type(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/facets-drawer/form/div/details[5]/div/div/label')    
  
@then("the bags according to Color are listed")  
def Color_Type_bags_listed(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/div[5]/span')  
        
    
# Scenario: checking for clear tab    

@when("the user clicks on clear tab")
def click_clear_Tab(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/div/a/span')


# Scenario: Adding product to wishlist

@when("user adds product to wishlist")
def product_whislisted(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/product-list/product-card[3]/div[1]/div/div/button/svg')
  
  
@when("user clicks on wishlist tab")
def product_whislist(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/header/height-observer/x-header/nav[2]/a[2]/svg')
  
@then("product is added in wishlist")  
def product_whislisted_added(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/div[17]/div[3]/div/div[2]/p/div/div/div[1]/div/div/p/div/div/span[1]/a')
    
# Scenario: deleting product from wishlist    

@when("click on remove all from wishlist")
def remove_product(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/div[18]/div[3]/div/div[2]/p/div/div/div[2]/button[2]/span[1]')
  
@when("click on OK")
def click_ok(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/div[19]/div[3]/div/div[3]/button[2]/span[1]') 
  
@then("wishlist must be empty")  
def wishlist_empty(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/div[18]/div[3]/div/div[2]/p/div/div/div/div') 
    
# Scenario: Adding product to cart    

@when("user adds product to cart")
def add_product_cart(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/product-list/product-card[2]/div[2]/form/button')
  
@then("product is added to cart")
def product_added(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/cart-drawer/p')


# Scenario: delete product from cart
    
@when("click on remove from cart")
def remove_product_cart(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/cart-drawer/div[1]/line-item/div/div/line-item-quantity/a')
  
@then("Now cart is empty")  
def empty_cart(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/cart-drawer/div[1]/line-item/div/div/line-item-quantity/a')   
    
 
# Scenario: sorting products Alphabetically A-Z   

@when("clicks on sort button")
def click_button_sort(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/height-observer/div/div[2]/button/span')
  
@when("selects sort Alphabetically A-Z")
def click_button_Alphabetically1(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/height-observer/div/div[2]/facets-sort-popover/x-listbox/button[3]/span')

@then("Products are Alphabetically sorted")  
def Alphabetically_sorted(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/product-list/product-card[1]/div[3]/div/div/a')
    
    
# Scenario:sorting products Price-low to high 
  
@when("selects sort Price-low to high")
def click_button_Price_low2high(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/height-observer/div/div[2]/facets-sort-popover/x-listbox/button[3]/span')

@then("Products are Price-low to high sorted")  
def price_sorted_low2high(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/product-list/product-card[1]/div[3]/div/div/price-list/sale-price')     
    

# Scenario: sorting products Date-old to new
  
@when("selects sort Date-old to new")
def click_button_old2new(variables):
  click_button(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/height-observer/div/div[2]/facets-sort-popover/x-listbox/button[7]/span')

@then("Products are Date-old to new sorted")  
def price_sorted_old2new(variables):
    get_element_text(variables["driver"], By.XPATH, '/html/body/main/section[3]/div/div/div/div/product-list/product-card[2]/div[3]/div/div/a')    