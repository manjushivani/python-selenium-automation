# Created by manju at 12/3/2024
  Feature: Tests for Cart

  Scenario: User can click cart icon
    Given Open target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown

 Scenario: User can signin on the target page
    Given Open target main page
    When Click Sign In
    Then From right side navigation menu, click Sign In
    Then Verify Sign In form opened
