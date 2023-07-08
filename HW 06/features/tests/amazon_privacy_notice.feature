# Created by kapam at 7/6/2023
Feature: Amazon privacy and notice tests

 Scenario: User can navigate to privacy and conditions link
   Given Open amazon main page
   When Click on button from SignIn popup
   Then Verify Sign In page opens
   And Click on Amazon Privacy & Condition Notice link
   And Store original windows
   And Click on Amazon Privacy Notice link
   And Switch to the newly opened window
   And Verify Amazon Privacy Notice page is opened
   And User can close new window and switch back to original
