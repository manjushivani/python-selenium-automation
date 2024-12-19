# Created by manju at 12/14/2024
Feature: Test 'Sign in' Target website
  # Enter feature description here

  Scenario: User can sign in target website
    Given Open target main page  # main page
    When  Click Sign In  # header
    Then  From right side navigation menu, click Sign In # header or create PO for menu
    Then  Verify Sign In form opened # sign in page

  Scenario: User can login in target website
    Given Open target main page  # main page
    When  Click Sign In  # header
    Then  From right side navigation menu, click Sign In # header or create PO for menu
    Then  Verify Sign In form opened # sign in page
    Then  enter email address
    Then  enter password
    Then  click on sign in button
    #Then click on next button
    #Then click on May be later button
    Then  verify user is logged in