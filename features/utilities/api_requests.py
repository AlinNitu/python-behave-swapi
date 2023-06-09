import requests

from features.utilities.api_commons import verify_status_code

"""
Customized api requests.
This way we can create request methods that can be overloaded depending on our test needs.
For example some requests might have params and others not, some requests might have headers and others not.
Or in some requests we might want to verify the response status code in a separate step to follow BDD standards,
while in some other cases we might use a request method as a precondition and we might want to check the response
code immediately in the request.
"""


def get_request(context, url, headers=None, params=None, response_code=None):
    """
    :param context:
    :param url:
    :param headers:
    :param params:
    :param response_code:
    :return:
    """
    context.response = requests.get(url=url, headers=headers, params=params, verify=False)
    verify_response_code(context, response_code)
    print(f"GET request response: {context.response.json()}")


def post_request(context, url, payload=None, headers=None, params=None, response_code=None, files=None):
    """
Example of POST request.
One example of re-usability is that a POST method can sometimes take a json payload as body,
or if we want to upload a file we can use the argument 'files'. This way we don't need to create
multiple methods for a POST request.
    :param context:
    :param url:
    :param payload:
    :param headers:
    :param params:
    :param response_code:
    :param files:
    :return:
    """
    context.res = requests.post(url=url, data=payload, headers=headers, params=params, files=files)
    verify_response_code(context, response_code)


def verify_response_code(context, response_code=None):
    """
    We want to verify the status code only if status code was passed as parameter in the request method.
    Otherwise, the status code will be verified in a separate step as per BDD principles.
    :param context:
    :param response_code:
    :return:
    """
    if response_code is not None:
        verify_status_code(context.response, response_code)
