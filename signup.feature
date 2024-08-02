Feature: Testing scenarios site sign up login cases

Scenario: Testing for Successful Sign Up
   Given the user is on the signup page
   When  entered valid user details
   Then  redirected to home page

Scenario: Successful login with valid credentials
    Given the user is on the login page
    When the user enters valid credentials
    When the user clicks on the login button
    Then the user should be redirected to the dashboard

Scenario: Sign Up with wrong password format 
   Given the user is on the signup page
   When  entered wrong password format
   Then Then the user should redirected to signup page

Scenario: Sign Up with wrong email format 
   Given the user is on the signup page
   When  entered wrong email format
   Then Then the user should redirected to signup page

Scenario: Testing if only Email is filled
   Given the user is on the login page
   When the user enters valid email id 
   When the user clicks on the login button
   Then the user should redirected to home page

Scenario: Testing if only password is filled
   Given the user is on the login page
   When the user enters valid password
   When the user clicks on the login button
   Then the user should redirected to home page



Scenario: Unsuccessful login with invalid credentials
    Given the user is on the login page
    When the user enters invalid credentials
    When the user clicks on the login button
    Then the user should redirected to home page  



Scenario: Unsuccessful login with empty fields
    Given the user is on the login page
    When the user leaves the username and password fields empty
    When the user clicks on the login button
    Then the user should redirected to home page

Scenario: Testing for forget password
    Given the user is on the login page
    When the user clicks on the forget password button
    Then the user should redirected to recover your password page
    

Scenario: Testing if mandatory fields are  not filled
   Given the user is on the login page
   When the user enters valid credentials
   When the user clicks on the login button
   Then the user should redirected to home page

Scenario: Check if the clicking on the bag button opens the bag option
   Given the user is on the login page
   When the user clicks on bag button
   Then the user should redirected to bag page


Scenario: Selecting bags according to price range from bag filter 
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on bag page filter
   When the user clicks on price tab
   When the user selects price
   When the user clicks on view result
   Then the bags according to price range are listed

Scenario: Selecting bags according to Product type
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on bag page filter
   When the user clicks on Product type tab
   When the user selects Product type
   When the user clicks on view result
   Then the bags according to product type are listed

Scenario: Selecting bags according to Pattern
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on bag page filter
   When the user clicks on Pattern tab
   When the user selects Pattern type
   When the user clicks on view result
   Then the bags according to Pattern are listed


Scenario: Selecting bags according to Occasion
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on bag page filter
   When the user clicks on Occasion tab
   When the user selects Occasion type
   When the user clicks on view result
   Then the bags according to Occasion are listed

Scenario: Selecting bags according to Category
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on bag page filter
   When the user clicks on Category tab
   When the user selects Category type
   When the user clicks on view result
   Then the bags according to Category are listed

Scenario: Selecting bags according to Color
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on bag page filter
   When the user clicks on Color tab
   When the user selects Color type
   When the user clicks on view result
   Then the bags according to Color are listed   

Scenario: checking for clear tab
   Given the user is on the login page
   When the user clicks on bag button
   When the user is on bag page
   When the user clicks on price tab
   When the user selects price
   When the user clicks on bag page filter
   When the user clicks on Product type tab
   When the user selects Product type
   When the user clicks on Pattern tab
   When the user selects Pattern type
   When the user clicks on Occasion tab
   When the user selects Occasion type
   When the user clicks on view result
   When the user clicks on clear tab  
   Then the user should redirected to bag page

Scenario: Adding product to wishlist
   Given the user is on the login page
   When user adds product to wishlist
   When user clicks on wishlist tab
   Then product is added in wishlist

Scenario: deleting product from wishlist
   Given the user is on the login page
   When user adds product to wishlist
   When user clicks on wishlist tab
   When click on remove all from wishlist
   When click on OK
   Then wishlist must be empty

Scenario: Adding product to cart
   Given the user is on the login page
   When user adds product to cart
   Then product is added to cart

Scenario: delete product from cart
   Given the user is on the login page
   When user adds product to cart
   When click on remove from cart
   Then Now cart is empty                           

Scenario: sorting products Alphabetically A-Z
   Given the user is on the login page
   When clicks on sort button
   When selects sort Alphabetically A-Z
   Then Products are Alphabetically sorted

Scenario: sorting products Price-low to high
   Given the user is on the login page
   When clicks on sort button
   When selects sort Price-low to high
   Then Products are Price-low to high sorted

Scenario: sorting products Date-old to new
   Given the user is on the login page
   When clicks on sort button
   When selects sort Date-old to new
   Then Products are Date-old to new sorted
