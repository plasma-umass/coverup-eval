# file tornado/escape.py:395-399
# lines [395, 396, 397, 398, 399]
# branches ['397->398', '397->399']

import pytest
from unittest import mock
import html.entities
from tornado.escape import _build_unicode_map

def test_build_unicode_map(mocker):
    # Mock the html.entities.name2codepoint to control the input
    mock_name2codepoint = {
        'quot': 34,
        'amp': 38,
        'lt': 60,
        'gt': 62,
    }
    mocker.patch.object(html.entities, 'name2codepoint', mock_name2codepoint)

    # Call the function
    result = _build_unicode_map()

    # Verify the result
    expected_result = {
        'quot': '"',
        'amp': '&',
        'lt': '<',
        'gt': '>',
    }
    assert result == expected_result

    # Clean up is handled by pytest-mock automatically

