Feature: OrangeHRM Logo
  Scenario: Logo presence on orange hrm homepage
    Given launch chrome browser
    When open orange hrm homepage
    And enter username "Admin" password "admin123"
    And click on login button
    Then user must successfully login to Dashboard page
