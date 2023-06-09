"""
Common methods
"""


def verify_status_code(response, expected_status_code):
    """
    :param response:
    :param expected_status_code:
    :return:
    """
    assert response.status_code == int(expected_status_code), \
        f"Expected status code {expected_status_code}, but the result was {response.status_code} " \
        f"with body {response.text}"
    