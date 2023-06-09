Feature: People endpoint from SWAPI open API
  """
  Querying /people endpoint by a specific search string and retrieve matching results.
  This feature file is to demonstrate how a real life scenario looks like but this functionality is covered
  in all_endpoints_in_one_scenario.feature file.
  """

  Scenario: End to end flow - Perform a successful search for people resources by a specific search parameter and then
            access the detailed url of each returned resource and verify their response
    When send a GET request to /people endpoint and search for Skywalker
    Then verify response status code 200
    And verify Skywalker is present in the response body
    When verify the detailed url of the returned resources contain Skywalker and has response code 200


  Scenario: When no element is found by the search query, return 200 status code, count 0 and empty results array
    When send a GET request to /people endpoint and search for Frodo Baggins
    Then verify response status code 200
    And verify an empty array is returned in response
    And verify a count of 0 is returned in response
    