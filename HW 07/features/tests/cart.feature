# Created by kapam at 7/26/2023
Feature: Shopping cart test

Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify Shopping Cart is empty