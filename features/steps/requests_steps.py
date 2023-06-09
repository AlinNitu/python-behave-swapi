from behave import step

from features.utilities.api_config import ApiConfig
from features.utilities.api_requests import get_request

"""
Some of the logic in the steps layer should be moved to a separate layer for better re-usability but for the purpose 
of this task it should be fine like this.
"""


@step("send a GET request to {expected_endpoint} endpoint and search for {search_parameter}")
def step_impl(context, expected_endpoint, search_parameter):
    url = f"{ApiConfig.BASE_URL}{expected_endpoint}"
    params = {"search": search_parameter}
    get_request(context=context,
                url=url,
                params=params)


@step("send a GET request to {expected_endpoint} endpoint")
def step_impl(context, expected_endpoint):
    url = f"{ApiConfig.BASE_URL}{expected_endpoint}"
    get_request(context=context, url=url)


@step("verify the detailed url of the returned resources contain {searched_parameter} and has response code {res_code}")
def step_impl(context, searched_parameter, res_code):
    """
    In this step we loop through the returned elements from the previous request, we access the detailed url of each
    resource, we send another request to that url and verify the status code the initially searched element to make
    sure that we returned the desired element.
    """
    response_results = context.response.json()['results']
    for item in response_results:
        detailed_url = item['url']
        get_request(context=context,
                    url=detailed_url,
                    response_code=res_code)
        assert searched_parameter in item['name'], \
            f"Element {searched_parameter} not found in detailed response body"
