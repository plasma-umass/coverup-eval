# file: lib/ansible/cli/arguments/option_helpers.py:243-274
# asked: {"lines": [243, 245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274], "branches": []}
# gained: {"lines": [243, 245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274], "branches": []}

import pytest
from unittest.mock import patch
from argparse import ArgumentParser, ArgumentError

# Mocking the constants
class MockConstants:
    DEFAULT_PRIVATE_KEY_FILE = '/path/to/default/private/key'
    DEFAULT_REMOTE_USER = 'default_user'
    DEFAULT_TRANSPORT = 'ssh'
    DEFAULT_TIMEOUT = 10
    DEFAULT_ASK_PASS = False
    CONNECTION_PASSWORD_FILE = '/path/to/connection/password/file'

# Mocking the unfrack_path function
def mock_unfrack_path():
    return lambda x: x

# Patching the constants and unfrack_path in the module
@patch('ansible.cli.arguments.option_helpers.C', new=MockConstants)
@patch('ansible.cli.arguments.option_helpers.unfrack_path', new=mock_unfrack_path)
def test_add_connect_options():
    from ansible.cli.arguments.option_helpers import add_connect_options

    parser = ArgumentParser()
    add_connect_options(parser)
    
    # Test without mutually exclusive arguments conflict
    args = parser.parse_args([
        '--private-key', '/custom/private/key',
        '-u', 'custom_user',
        '-c', 'paramiko',
        '-T', '20',
        '--ssh-common-args', 'common_args',
        '--sftp-extra-args', 'sftp_args',
        '--scp-extra-args', 'scp_args',
        '--ssh-extra-args', 'ssh_args',
        '--connection-password-file', '/custom/connection/password/file'
    ])
    
    assert args.private_key_file == '/custom/private/key'
    assert args.remote_user == 'custom_user'
    assert args.connection == 'paramiko'
    assert args.timeout == 20
    assert args.ssh_common_args == 'common_args'
    assert args.sftp_extra_args == 'sftp_args'
    assert args.scp_extra_args == 'scp_args'
    assert args.ssh_extra_args == 'ssh_args'
    assert args.ask_pass is False
    assert args.connection_password_file == '/custom/connection/password/file'
    
    # Test with mutually exclusive arguments conflict
    with pytest.raises(SystemExit):
        parser.parse_args([
            '--private-key', '/custom/private/key',
            '-u', 'custom_user',
            '-c', 'paramiko',
            '-T', '20',
            '--ssh-common-args', 'common_args',
            '--sftp-extra-args', 'sftp_args',
            '--scp-extra-args', 'scp_args',
            '--ssh-extra-args', 'ssh_args',
            '-k',
            '--connection-password-file', '/custom/connection/password/file'
        ])
