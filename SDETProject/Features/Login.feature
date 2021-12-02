Feature: Login
  Scenario: Login and insert data into DB
    Given launch chrome browser
    When open html page
    And enter Name "Neha F" UID "U100" Company Name "UST" Email "nehafc@ust.com"
    And click on login button
    Then user must successfully login to Display page