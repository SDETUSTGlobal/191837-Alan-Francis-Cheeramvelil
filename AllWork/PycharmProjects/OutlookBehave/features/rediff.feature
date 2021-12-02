Feature: Outlook Login
  Scenario: Navigate to Outlook and login
     Given  chrome is launched
    When we navigate to Rediff website
    And we enter username "afc2702@gmail.com" password "test"
    And we press the login button
    Then we successfully navigate tologin incorrect page
