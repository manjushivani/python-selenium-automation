# Created by manju at 12/13/2024
Feature: Cart empty test
  # Enter feature description here

 Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    Then Click on Cart icon
    Then Verify 'Your cart is empty' message is shown
