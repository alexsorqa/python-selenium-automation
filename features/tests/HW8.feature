# Created by asorokin at 4/5/23
Feature: Test Scenarios for HW8.1 and HW8.2


  Scenario: User can select and search in a department
    Given Opens Amazon page
    When Select department by alias Video Games
    When Input text New World
    When Clicks on search icon
    Then Verify videogames department is selected


  Scenario: User can see any deals after hovering over New Arivals
    Given Opens Cat Hoodie page
    When User hovers over New Arrivals
    Then 6 deals are displayed