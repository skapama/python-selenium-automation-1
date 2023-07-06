# Created by kapam at 7/6/2023
Feature: Amazon search tests
  # Enter feature description here

    |coffee           |"coffee"         |
    |mug              |"mug"            |
    |dress            |"dress"          |

  Scenario: User can add a product to the cart
    Given Open amazon main page
    When Search for Tritan Farm to Table Pitcher
    And Click on the first product
    And Store product name
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product