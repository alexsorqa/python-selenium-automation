# Created by bonum at 2/20/2023
Feature: Amazon cart tests

  Scenario: Verify Amazon Cart is empty
    Given Open Amazon page
    When Click on Cart icon
    Then Amazon cart page is displayed
    And Your Amazon Cart is empty text shown