# file thefuck/logs.py:12-17
# lines [12, 14, 15, 17]
# branches ['14->15', '14->17']

import pytest
from unittest import mock

# Assuming the settings object is part of thefuck module
class MockSettings:
    def __init__(self, no_colors):
        self.no_colors = no_colors

@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.logs.settings', new_callable=lambda: MockSettings(no_colors=False))

def test_color_with_colors(mock_settings):
    from thefuck.logs import color
    mock_settings.no_colors = False
    assert color('red') == 'red'

def test_color_without_colors(mock_settings):
    from thefuck.logs import color
    mock_settings.no_colors = True
    assert color('red') == ''

