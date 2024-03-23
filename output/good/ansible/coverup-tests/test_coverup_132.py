# file lib/ansible/cli/arguments/option_helpers.py:243-274
# lines [243, 245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.constants import DEFAULT_PRIVATE_KEY_FILE, DEFAULT_REMOTE_USER, DEFAULT_TRANSPORT, DEFAULT_TIMEOUT, DEFAULT_ASK_PASS, CONNECTION_PASSWORD_FILE
from ansible.cli.arguments.option_helpers import add_connect_options
from argparse import ArgumentParser

# Mock the unfrack_path function
def mock_unfrack_path():
    return lambda x: x

@pytest.fixture
def parser():
    # Create a parser object and return it
    return ArgumentParser(description="Test Parser")

@pytest.fixture
def mock_constants(mocker):
    # Mock the constants with default values
    mocker.patch('ansible.constants.DEFAULT_PRIVATE_KEY_FILE', 'default_key')
    mocker.patch('ansible.constants.DEFAULT_REMOTE_USER', 'default_user')
    mocker.patch('ansible.constants.DEFAULT_TRANSPORT', 'default_transport')
    mocker.patch('ansible.constants.DEFAULT_TIMEOUT', 10)
    mocker.patch('ansible.constants.DEFAULT_ASK_PASS', False)
    mocker.patch('ansible.constants.CONNECTION_PASSWORD_FILE', 'conn_pass_file')

def test_add_connect_options(parser, mock_constants, mocker):
    # Mock the unfrack_path function in the module
    mocker.patch('ansible.cli.arguments.option_helpers.unfrack_path', mock_unfrack_path)

    # Call the function to add connection options
    add_connect_options(parser)

    # Parse arguments with default values
    args = parser.parse_args([])

    # Assertions to check if the default values are set correctly
    assert args.private_key_file == 'default_key'
    assert args.remote_user == 'default_user'
    assert args.connection == 'default_transport'
    assert args.timeout == 10
    assert args.ask_pass == False
    assert args.connection_password_file == 'conn_pass_file'

    # Assertions to check if the ssh arguments are None by default
    assert args.ssh_common_args is None
    assert args.sftp_extra_args is None
    assert args.scp_extra_args is None
    assert args.ssh_extra_args is None

    # Parse arguments with non-default values
    custom_args = [
        '--private-key', 'custom_key',
        '--user', 'custom_user',
        '--connection', 'custom_transport',
        '--timeout', '20',
        '--ssh-common-args', 'ssh_common',
        '--sftp-extra-args', 'sftp_extra',
        '--scp-extra-args', 'scp_extra',
        '--ssh-extra-args', 'ssh_extra',
        '--connection-password-file', 'custom_conn_pass_file'
    ]
    args = parser.parse_args(custom_args)

    # Assertions to check if the custom values are set correctly
    assert args.private_key_file == 'custom_key'
    assert args.remote_user == 'custom_user'
    assert args.connection == 'custom_transport'
    assert args.timeout == 20
    assert args.ssh_common_args == 'ssh_common'
    assert args.sftp_extra_args == 'sftp_extra'
    assert args.scp_extra_args == 'scp_extra'
    assert args.ssh_extra_args == 'ssh_extra'
    assert args.connection_password_file == 'custom_conn_pass_file'
