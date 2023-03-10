# Created by asorokin at 3/3/23
Feature: Test scenarios for adding items to cart

  Scenario: Cart items verification
    Given Open Amazon page
    When Click on Best sellers
    Then Click on water
    Then Water page is shown
    And Click on quantity
    And Select 3 items
    And Click on Add to Cart
    Then Click on Cart icon
    And 3 items are added