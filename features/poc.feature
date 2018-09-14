@Feature1
Feature: As a QA engineer, I want to demo basic functionality of Behave

@Test_Scenario
  Scenario: Empty Behave steps should pass as an example
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!

@Test_FBG_Title
  Scenario: Feedback Genius title should display expected results
    Given I visit the Feedback Genius page
    Then the title should say "Feedback Genius - Amazon Seller Feedback Software"

#
# @params
# Scenario: look up a book
#    Then the result page will include "success"
#
#
# @params
# Scenario: look up an invalid book
#    Then the result page will include "failure"
#
#
# @Test_Scenario_Outline
#   Scenario Outline: Blenders
#     Given I put <thing> in a blender,
#     When I switch the blender on
#     Then it should transform into <other thing>
#
#  Examples: Amphibians
#    | thing         | other thing |
#    | Red Tree Frog | mush        |
#
#  Examples: Consumer Electronics
#    | thing         | other thing |
#    | iPhone        | toxic waste |
#    | Galaxy Nexus  | toxic waste |
#
#
# @Test_Step_Data
#   Scenario: some scenario
#   Given a sample text loaded into the frobulator
#      """
#      Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
#      eiusmod tempor incididunt ut labore et dolore magna aliqua.
#      """
#  When we activate the frobulator
#  Then we will find it similar to English
