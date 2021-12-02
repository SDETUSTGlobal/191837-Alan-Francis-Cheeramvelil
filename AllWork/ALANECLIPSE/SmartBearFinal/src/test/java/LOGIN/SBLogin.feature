Feature: Login
Background: 
Given user on the login page  
And user follows "Log in"  

Scenario: Verification of Login Function  
Given user on the Login Page
And user enters "username" with "Tester" 
And user enters "password" with "test"  
And user click "log in" button
Then user should see "Web Orders" 
Scenario: Unsuccessful login
Given user on the Login Page
And user enters "username" with "Tester" 
And user enters "password" with "tester"  
And user clicks "login" button
Then error message displayed with wrong password
And user returns back on login page
