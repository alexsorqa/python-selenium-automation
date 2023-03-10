# Created by asorokin at 3/3/23
Feature: Test scenarios for best sellers page

  Scenario: Best sellers submenu verification
    Given Open Amazon page
    When Click on best sellers
    Then 5 submenus are displayed