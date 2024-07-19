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

