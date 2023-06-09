Feature: Testing the search functionality of all endpoints using only one scenario
  """
  In a real life scenario this case is very unlikely because the endpoints will be more complex, we need to mock data,
  we use dynamic path and query parameters and so on.
  However, due to the way SWAPI is designed I have also designed the framework to be extremely modular and reusable
  so we can basically use one scenario to cover all endpoints per functionality tested.
  """

  Scenario Outline: End to end flow - test the search functionality of all endpoints and verify
                    response status code and body
    When send a GET request to <endpoint> endpoint and search for <search_query>
    Then verify response status code 200
    And verify <search_query> is present in the response body
    When verify the detailed url of the returned resources contain <search_query> and has response code 200
    Examples:
      | endpoint    | search_query  |
      | /people     | Skywalker     |
      | /planets    | Tatooine      |
      | /starships  | Death Star    |
      | /vehicles   | Sail barge    |



  Scenario Outline: Test all endpoints when they return all results by default
    When send a GET request to <endpoint> endpoint
    Then verify response status code 200
    And verify response body for the requested endpoint
    Examples:
      | endpoint    |
      | /people     |
      | /planets    |
      | /starships  |
      | /vehicles   |
