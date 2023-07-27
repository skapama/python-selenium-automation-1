Feature: Amazon product search

Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon main page
 When Click Amazon Orders link
 Then Verify Sign In page opens
