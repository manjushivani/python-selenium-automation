# Created by manju at 12/3/2024
  Feature: Tests for search

  Scenario: User can search for product
    Given Open target main page
    When Search for teddy bear
    #Then Verify search results shown
    #Then Verify search results shown for teddy bear


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for coffee
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    When Verify cart has 1 item(s)
    And Verify cart has correct product