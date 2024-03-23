# file mimesis/providers/internet.py:59-67
# lines [59, 67]
# branches []

import pytest
from mimesis.providers.internet import Internet
from mimesis.data import HTTP_STATUS_MSGS

def test_http_status_message():
    internet_provider = Internet()

    # Call the method under test
    status_message = internet_provider.http_status_message()

    # Assert that the returned status message is in the list of HTTP_STATUS_MSGS
    assert status_message in HTTP_STATUS_MSGS
