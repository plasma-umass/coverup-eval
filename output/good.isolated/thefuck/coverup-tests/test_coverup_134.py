# file thefuck/logs.py:93-114
# lines []
# branches ['107->114']

import pytest
from thefuck.logs import how_to_configure_alias
from collections import namedtuple
from unittest.mock import patch
import colorama


@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')


@pytest.fixture
def configuration_details():
    ConfigDetails = namedtuple('ConfigDetails', ['can_configure_automatically', 'content', 'path', 'reload'])
    return ConfigDetails(can_configure_automatically=False, content='content', path='path', reload='reload')


def test_how_to_configure_alias_without_automatic_configuration(mock_print, configuration_details):
    how_to_configure_alias(configuration_details)
    assert mock_print.call_count == 3
    mock_print.assert_any_call(u"Seems like {bold}fuck{reset} alias isn't configured!".format(
        bold=colorama.Style.BRIGHT,
        reset=colorama.Style.RESET_ALL))
    mock_print.assert_any_call(
        u"Please put {bold}{content}{reset} in your "
        u"{bold}{path}{reset} and apply "
        u"changes with {bold}{reload}{reset} or restart your shell.".format(
            bold=colorama.Style.BRIGHT,
            reset=colorama.Style.RESET_ALL,
            **configuration_details._asdict()))
    mock_print.assert_any_call(u'More details - https://github.com/nvbn/thefuck#manual-installation')
