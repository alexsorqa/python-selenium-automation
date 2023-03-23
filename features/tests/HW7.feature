# Created by asorokin at 3/20/23
Feature: Test Scenarios for HW7.1, HW7.2

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Opens Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened



  Scenario: 'Your Shopping Cart is empty' shown if no product added
    Given Opens Amazon page
    When Clicks on cart icon
    Then Verify 'Your Shopping Cart is empty.' text present


  Scenario: “Add a product to cart”
    Given Opens Amazon page
    When Search for product
    Then Product results page is displayed
    And Click on first item
    Then Product page is displayed
    When Selects size
    And  Add to Cart
    And  Clicks on Cart icon
    Then Cart page is displayed
