# Created by bonum at 2/20/2023
Feature: Sign In page tests

  Scenario: Logged out user sees sign in page
    Given Open Amazon page
    When Click orders
    Then Sign in page is displayed
    And Sign In header is visible
    And Email input field is present

