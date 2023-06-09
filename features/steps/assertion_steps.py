from behave import step

from features.utilities import api_commons


@step("verify response status code {status_code}")
def step_impl(context, status_code):
    api_commons.verify_status_code(context.response, status_code)


@step("verify {searched_parameter} is present in the response body")
def step_impl(context, searched_parameter):
    response_body = context.response.json()
    # we can have a separate layer for the assertion methods but for this assignment I will keep them in the step layer
    assert isinstance(response_body['results'], list)  # asserting 'results' field is an array
    for item in response_body['results']:
        assert searched_parameter in item['name'], \
            f"Element {searched_parameter} not found in the response body."


@step("verify an empty array is returned in response")
def step_impl(context):
    assert not context.response.json()['results'], "List is not empty"


@step("verify a count of {count} is returned in response")
def step_impl(context, count):
    assert context.response.json()['count'] == 0, f"Count is not {count}"


@step("verify response body for the requested endpoint")
def step_impl(context):
    """
    Ideally we split these assertions per multiple steps or when possible we create lists and compare the lists.
    """
    response_body = context.response.json()
    assert isinstance(response_body['count'], int)
    assert isinstance(response_body['results'], list)
    for item in response_body['results']:
        assert isinstance(item['name'], str)
        assert item['name'] is not None
        assert isinstance(item['url'], str)
        assert item['url'] is not None
