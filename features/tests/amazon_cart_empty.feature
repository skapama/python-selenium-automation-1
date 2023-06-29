# Created by kapama at 6/28/2023
Feature: Amazon cart empty tests

  Scenario: User can see cart empty
    Given Open amazon main page
    When Click Cart
    Then Verify cart is empty