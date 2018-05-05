# -- FILE: features/example.feature
Feature: Showing off behave
  Scenario: Testing selenium
    Given I fire up a web browser
     When I hit the keys
     Then its all ok

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!