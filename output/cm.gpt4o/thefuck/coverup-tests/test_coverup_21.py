# file thefuck/logs.py:127-134
# lines [127, 128, 129, 131, 132, 133, 134]
# branches []

import pytest
from unittest import mock
from thefuck.logs import configured_successfully
import colorama

@pytest.fixture
def mock_colorama(mocker):
    mocker.patch('colorama.Style.BRIGHT', 'BRIGHT')
    mocker.patch('colorama.Style.RESET_ALL', 'RESET_ALL')

def test_configured_successfully(mock_colorama, capsys):
    configuration_details = mock.Mock()
    configuration_details.reload = 'source ~/.bashrc'

    configured_successfully(configuration_details)

    captured = capsys.readouterr()
    expected_output = (
        "BRIGHTfuckRESET_ALL alias configured successfully!\n"
        "For applying changes run BRIGHTsource ~/.bashrcRESET_ALL"
        " or restart your shell.\n"
    )
    assert captured.out == expected_output
