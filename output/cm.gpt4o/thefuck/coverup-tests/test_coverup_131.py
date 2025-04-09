# file thefuck/logs.py:117-124
# lines [118, 119, 121, 122, 123, 124]
# branches []

import pytest
from unittest import mock
from thefuck.logs import already_configured

def test_already_configured(mocker):
    # Mocking colorama.Style.BRIGHT and colorama.Style.RESET_ALL
    mocker.patch('thefuck.logs.colorama.Style.BRIGHT', 'BRIGHT')
    mocker.patch('thefuck.logs.colorama.Style.RESET_ALL', 'RESET')
    
    # Mocking the color function
    mocker.patch('thefuck.logs.color', side_effect=lambda x: x)
    
    # Mocking the print function
    mock_print = mocker.patch('builtins.print')
    
    # Creating a mock configuration_details object
    configuration_details = mock.Mock()
    configuration_details.reload = 'reload_command'
    
    # Calling the function
    already_configured(configuration_details)
    
    # Asserting the print function was called with the expected string
    mock_print.assert_called_once_with(
        u"Seems like BRIGHTfuckRESET alias already configured!\n"
        u"For applying changes run BRIGHTreload_commandRESET"
        u" or restart your shell."
    )
