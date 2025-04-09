# file: lib/ansible/cli/arguments/option_helpers.py:243-274
# asked: {"lines": [243, 245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274], "branches": []}
# gained: {"lines": [243, 245, 247, 248, 249, 250, 251, 252, 253, 254, 257, 258, 259, 260, 261, 262, 263, 264, 266, 268, 269, 270, 271, 272, 274], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_connect_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_connect_options(parser, monkeypatch):
    def mock_unfrack_path():
        return lambda x: x

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', mock_unfrack_path)
    add_connect_options(parser)
    args = parser.parse_args([])

    assert args.private_key_file == C.DEFAULT_PRIVATE_KEY_FILE
    assert args.remote_user == C.DEFAULT_REMOTE_USER
    assert args.connection == C.DEFAULT_TRANSPORT
    assert args.timeout == C.DEFAULT_TIMEOUT
    assert args.ssh_common_args is None
    assert args.sftp_extra_args is None
    assert args.scp_extra_args is None
    assert args.ssh_extra_args is None
    assert args.ask_pass == C.DEFAULT_ASK_PASS
    assert args.connection_password_file == C.CONNECTION_PASSWORD_FILE

def test_add_connect_options_with_args(parser, monkeypatch):
    def mock_unfrack_path():
        return lambda x: x

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', mock_unfrack_path)
    test_args = [
        '--private-key', 'test_key',
        '-u', 'test_user',
        '-c', 'test_connection',
        '-T', '30',
        '--ssh-common-args', 'test_ssh_common_args',
        '--sftp-extra-args', 'test_sftp_extra_args',
        '--scp-extra-args', 'test_scp_extra_args',
        '--ssh-extra-args', 'test_ssh_extra_args',
        '--connection-password-file', 'test_conn_pass_file'
    ]
    add_connect_options(parser)
    args = parser.parse_args(test_args)

    assert args.private_key_file == 'test_key'
    assert args.remote_user == 'test_user'
    assert args.connection == 'test_connection'
    assert args.timeout == 30
    assert args.ssh_common_args == 'test_ssh_common_args'
    assert args.sftp_extra_args == 'test_sftp_extra_args'
    assert args.scp_extra_args == 'test_scp_extra_args'
    assert args.ssh_extra_args == 'test_ssh_extra_args'
    assert args.ask_pass is False
    assert args.connection_password_file == 'test_conn_pass_file'

def test_add_connect_options_with_ask_pass(parser, monkeypatch):
    def mock_unfrack_path():
        return lambda x: x

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.unfrack_path', mock_unfrack_path)
    test_args = [
        '--private-key', 'test_key',
        '-u', 'test_user',
        '-c', 'test_connection',
        '-T', '30',
        '--ssh-common-args', 'test_ssh_common_args',
        '--sftp-extra-args', 'test_sftp_extra_args',
        '--scp-extra-args', 'test_scp_extra_args',
        '--ssh-extra-args', 'test_ssh_extra_args',
        '-k'
    ]
    add_connect_options(parser)
    args = parser.parse_args(test_args)

    assert args.private_key_file == 'test_key'
    assert args.remote_user == 'test_user'
    assert args.connection == 'test_connection'
    assert args.timeout == 30
    assert args.ssh_common_args == 'test_ssh_common_args'
    assert args.sftp_extra_args == 'test_sftp_extra_args'
    assert args.scp_extra_args == 'test_scp_extra_args'
    assert args.ssh_extra_args == 'test_ssh_extra_args'
    assert args.ask_pass is True
    assert args.connection_password_file == C.CONNECTION_PASSWORD_FILE
