# Created by asorokin at 3/7/23
Feature: Test Scenarios for hoodie

  Scenario: Hoodie variety verification
    Given Open Amazon page
    When Search for hoodie
    Then Select hoodie
    Then Hoodie page is displayed
    And All colors are presented