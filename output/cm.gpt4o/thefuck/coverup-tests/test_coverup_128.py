# file thefuck/logs.py:93-114
# lines []
# branches ['107->114']

import pytest
from unittest import mock
from thefuck.logs import how_to_configure_alias

def test_how_to_configure_alias_with_auto_config(mocker):
    # Mocking the configuration_details object
    configuration_details = mock.Mock()
    configuration_details.can_configure_automatically = True
    configuration_details._asdict.return_value = {
        'content': 'eval $(thefuck --alias)',
        'path': '~/.bashrc',
        'reload': 'source ~/.bashrc'
    }

    # Mocking the print function to capture print statements
    mock_print = mocker.patch('builtins.print')

    # Call the function with the mocked configuration_details
    how_to_configure_alias(configuration_details)

    # Assertions to verify the correct print statements
    mock_print.assert_any_call(
        u"Seems like \x1b[1mfuck\x1b[0m alias isn't configured!"
    )
    mock_print.assert_any_call(
        u"Please put \x1b[1meval $(thefuck --alias)\x1b[0m in your "
        u"\x1b[1m~/.bashrc\x1b[0m and apply "
        u"changes with \x1b[1msource ~/.bashrc\x1b[0m or restart your shell."
    )
    mock_print.assert_any_call(
        u"Or run \x1b[1mfuck\x1b[0m a second time to configure"
        u" it automatically."
    )
    mock_print.assert_any_call(
        u'More details - https://github.com/nvbn/thefuck#manual-installation'
    )

def test_how_to_configure_alias_without_auto_config(mocker):
    # Mocking the configuration_details object
    configuration_details = mock.Mock()
    configuration_details.can_configure_automatically = False
    configuration_details._asdict.return_value = {
        'content': 'eval $(thefuck --alias)',
        'path': '~/.bashrc',
        'reload': 'source ~/.bashrc'
    }

    # Mocking the print function to capture print statements
    mock_print = mocker.patch('builtins.print')

    # Call the function with the mocked configuration_details
    how_to_configure_alias(configuration_details)

    # Assertions to verify the correct print statements
    mock_print.assert_any_call(
        u"Seems like \x1b[1mfuck\x1b[0m alias isn't configured!"
    )
    mock_print.assert_any_call(
        u"Please put \x1b[1meval $(thefuck --alias)\x1b[0m in your "
        u"\x1b[1m~/.bashrc\x1b[0m and apply "
        u"changes with \x1b[1msource ~/.bashrc\x1b[0m or restart your shell."
    )
    mock_print.assert_any_call(
        u'More details - https://github.com/nvbn/thefuck#manual-installation'
    )
