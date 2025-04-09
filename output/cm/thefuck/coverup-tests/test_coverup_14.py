# file thefuck/logs.py:117-124
# lines [117, 118, 119, 121, 122, 123, 124]
# branches []

import pytest
from thefuck.logs import already_configured
from unittest.mock import patch
import colorama


@pytest.fixture
def mock_colorama(mocker):
    mocker.patch('thefuck.logs.colorama.Style.BRIGHT', 'BRIGHT')
    mocker.patch('thefuck.logs.colorama.Style.RESET_ALL', 'RESET_ALL')


@pytest.fixture
def mock_print(mocker):
    return mocker.patch('thefuck.logs.print')


@pytest.fixture
def configuration_details():
    class ConfigDetails:
        def __init__(self):
            self.reload = 'some_reload_command'

    return ConfigDetails()


def test_already_configured(mock_colorama, mock_print, configuration_details):
    already_configured(configuration_details)
    expected_message = (
        u"Seems like BRIGHTfuckRESET_ALL alias already configured!\n"
        u"For applying changes run BRIGHTsome_reload_commandRESET_ALL"
        u" or restart your shell."
    )
    mock_print.assert_called_once_with(expected_message)
