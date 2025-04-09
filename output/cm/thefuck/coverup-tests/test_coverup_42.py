# file thefuck/logs.py:12-17
# lines [12, 14, 15, 17]
# branches ['14->15', '14->17']

import pytest
from thefuck.logs import color
from thefuck.conf import settings
from unittest.mock import patch

# Assuming the settings module has a 'no_colors' attribute that can be set.

@pytest.fixture
def no_colors_enabled():
    original_value = settings.no_colors
    settings.no_colors = True
    yield
    settings.no_colors = original_value

@pytest.fixture
def no_colors_disabled():
    original_value = settings.no_colors
    settings.no_colors = False
    yield
    settings.no_colors = original_value

def test_color_function_with_no_colors_enabled(no_colors_enabled):
    # Call the color function with any color argument
    result = color('some_color_code')

    # Assert that the result is an empty string when no_colors is enabled
    assert result == ''

def test_color_function_with_no_colors_disabled(no_colors_disabled):
    # Call the color function with any color argument
    result = color('some_color_code')

    # Assert that the result is the color code when no_colors is disabled
    assert result == 'some_color_code'
