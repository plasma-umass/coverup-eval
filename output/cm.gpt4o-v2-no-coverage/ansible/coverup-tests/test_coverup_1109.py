# file: lib/ansible/cli/arguments/option_helpers.py:243-274
# asked: {"lines": [245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274], "branches": []}
# gained: {"lines": [245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274], "branches": []}

import pytest
from unittest.mock import MagicMock
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_connect_options
from ansible import constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def mock_unfrack_path(path):
    return path

def test_add_connect_options(parser, monkeypatch):
    # Mock constants
    monkeypatch.setattr(C, 'DEFAULT_PRIVATE_KEY_FILE', '/path/to/default/private/key')
    monkeypatch.setattr(C, 'DEFAULT_REMOTE_USER', 'default_user')
    monkeypatch.setattr(C, 'DEFAULT_TRANSPORT', 'ssh')
    monkeypatch.setattr(C, 'DEFAULT_TIMEOUT', 10)
    monkeypatch.setattr(C, 'DEFAULT_ASK_PASS', False)
    monkeypatch.setattr(C, 'CONNECTION_PASSWORD_FILE', '/path/to/connection/password/file')

    # Mock unfrack_path
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', lambda: mock_unfrack_path)

    add_connect_options(parser)
    args = parser.parse_args([])

    assert args.private_key_file == '/path/to/default/private/key'
    assert args.remote_user == 'default_user'
    assert args.connection == 'ssh'
    assert args.timeout == 10
    assert args.ssh_common_args is None
    assert args.sftp_extra_args is None
    assert args.scp_extra_args is None
    assert args.ssh_extra_args is None
    assert args.ask_pass is False
    assert args.connection_password_file == '/path/to/connection/password/file'
