# Created by kapam at 7/6/2023
Feature: Amazon privacy and notice tests


Scenario: User can open and close Amazon Privacy Notice
 Given Open Amazon T&C page
 When Store original windows
 And Click on Amazon Privacy Notice link
 And Switch to the newly opened window
 Then Verify Amazon Privacy Notice page is opened
 And Use can close new window and switch back to original
