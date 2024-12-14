# Created by manju at 12/3/2024
  Feature: Tests for search

  Scenario: User can search for product
    Given Open target main page
    When Search for teddy bear
    And Verify search results shown
    Then Verify search results shown for teddy bear


  Scenario: User can add a product to cart
    Given Open target main page
    When Search for shoes
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Store product name
    And Open cart page
    When Verify cart has 1 item(s)
    And Verify cart has correct product


  Scenario Outline: User can search for a product
    Given Open target main page
    When Search for <product>
    Then Verify search results shown for <product>
    Examples:
    |product    |
    |coffee     |
    |tea        |
    |mug        |


  Scenario: Verify that user can see product names and images
    Given Open target main page
    When Search for AirPods (3rd Generation)
    Then Verify that every product has a name and an image


 Scenario: 'Your cart is empty' message is shown for empty cart
    Given Open target main page
    Then Click on Cart icon
    Then Verify 'Your cart is empty' message is shown

