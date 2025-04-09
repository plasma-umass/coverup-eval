# file thefuck/logs.py:127-134
# lines [127, 128, 129, 131, 132, 133, 134]
# branches []

import pytest
from thefuck.logs import configured_successfully
from unittest.mock import patch
import colorama


@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')


@pytest.fixture
def mock_color(mocker):
    return mocker.patch('thefuck.logs.color', side_effect=lambda x: x)


@pytest.fixture
def configuration_details():
    class ConfigDetails:
        def __init__(self):
            self.reload = 'source ~/.bashrc'
    return ConfigDetails()


def test_configured_successfully(mock_print, mock_color, configuration_details):
    configured_successfully(configuration_details)
    mock_color.assert_any_call(colorama.Style.BRIGHT)
    mock_color.assert_any_call(colorama.Style.RESET_ALL)
    mock_print.assert_called_once_with(
        u"{bold}fuck{reset} alias configured successfully!\n"
        u"For applying changes run {bold}{reload}{reset}"
        u" or restart your shell.".format(
            bold=colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            reload=configuration_details.reload))
