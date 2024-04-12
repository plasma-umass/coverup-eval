# file tornado/locale.py:219-221
# lines [219, 221]
# branches []

import pytest
from tornado.locale import get_supported_locales, _supported_locales

def test_get_supported_locales(mocker):
    # Mock the _supported_locales variable
    mock_locales = ['en_US', 'es_ES']
    mocker.patch('tornado.locale._supported_locales', mock_locales)

    # Call the function under test
    supported_locales = get_supported_locales()

    # Check that the function returns the mocked list
    assert list(supported_locales) == mock_locales

    # Clean up by unpatching
    mocker.stopall()
