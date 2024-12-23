# Created by manju at 12/22/2024
Feature:  Create a window handling test case from the class

  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    When Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And Close current page
    And Return to original window

