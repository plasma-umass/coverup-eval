# file lib/ansible/plugins/connection/paramiko_ssh.py:252-295
# lines [252, 253, 255, 256, 257, 258, 261, 262, 263, 265, 268, 269, 270, 271, 273, 274, 276, 278, 279, 280, 281, 282, 283, 285, 286, 287, 288, 289, 290, 291, 295]
# branches ['262->263', '262->276', '263->265', '263->268', '269->270', '269->273', '270->271', '270->273', '273->262', '273->274', '279->280', '279->295', '285->286', '285->287']

import pytest
from unittest.mock import MagicMock
from ansible.plugins.connection.paramiko_ssh import Connection
from ansible.playbook.play_context import PlayContext
from ansible.utils.display import Display

# Mock SETTINGS_REGEX to simplify the test
@pytest.fixture
def mock_settings_regex(mocker):
    SETTINGS_REGEX = mocker.patch('ansible.plugins.connection.paramiko_ssh.SETTINGS_REGEX')
    SETTINGS_REGEX.match.side_effect = lambda x: mocker.Mock(group=lambda n: ('ProxyCommand', 'dummy_command')[n-1] if x == 'ProxyCommand dummy_command' else None)
    return SETTINGS_REGEX

# Mock paramiko and Display for the test
@pytest.fixture
def mock_paramiko_proxy_command(mocker):
    paramiko = mocker.patch('ansible.plugins.connection.paramiko_ssh.paramiko')
    paramiko.ProxyCommand = MagicMock()
    return paramiko.ProxyCommand

@pytest.fixture
def mock_display(mocker):
    display = mocker.patch('ansible.plugins.connection.paramiko_ssh.display')
    display.vvv = MagicMock()
    display.warning = MagicMock()
    return display

# Test function to improve coverage
def test_parse_proxy_command(mock_settings_regex, mock_paramiko_proxy_command, mock_display):
    play_context = PlayContext()
    play_context.remote_addr = 'remote_host'
    play_context.remote_user = 'remote_user'
    play_context.ssh_extra_args = ''
    play_context.ssh_common_args = 'ProxyCommand dummy_command'
    play_context.ssh_args = ''

    connection = Connection(play_context, new_stdin=False)

    sock_kwarg = connection._parse_proxy_command(port=22)

    # Assertions to verify postconditions
    assert mock_paramiko_proxy_command.called
    assert mock_display.vvv.called
    assert sock_kwarg == {'sock': mock_paramiko_proxy_command.return_value}

    # Clean up
    mock_paramiko_proxy_command.reset_mock()
    mock_display.vvv.reset_mock()
    mock_display.warning.reset_mock()

# Test function to cover the case where Paramiko ProxyCommand support is unavailable
def test_parse_proxy_command_no_paramiko_proxy_command(mock_settings_regex, mock_display, mocker):
    mocker.patch('ansible.plugins.connection.paramiko_ssh.paramiko', None)

    play_context = PlayContext()
    play_context.remote_addr = 'remote_host'
    play_context.remote_user = 'remote_user'
    play_context.ssh_extra_args = ''
    play_context.ssh_common_args = 'ProxyCommand dummy_command'
    play_context.ssh_args = ''

    connection = Connection(play_context, new_stdin=False)

    sock_kwarg = connection._parse_proxy_command(port=22)

    # Assertions to verify postconditions
    assert mock_display.warning.called
    assert sock_kwarg == {}

    # Clean up
    mock_display.vvv.reset_mock()
    mock_display.warning.reset_mock()
