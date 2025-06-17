Feature: OrangeHRM Login

Background:
Given the user is on the OrangeHRM login page

@positive
  Scenario Outline: Login with valid credentials
    #Given the user is on the OrangeHRM login page
    When the user enters username "<username>" and password "<password>"
    Then the user should be redirected to the dashboard

    Examples:
      | username | password |
      | Admin    | admin123 |

@negative @security
Scenario Outline: Login with invalid credentials
  #Given the user is on the OrangeHRM login page
  When the user enters username "<username>" and password "<password>"
  Then the user should see an error message "<error_message>"

Examples:
  | username | password   | error_message       |
  | Admin    | wrongness  | Invalid credentials |
  | wronger  | admin123   | Invalid credentials |
  | typoUser | admin123   | Invalid credentials |

