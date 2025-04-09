# file: lib/ansible/cli/vault.py:52-118
# asked: {"lines": [52, 53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118], "branches": []}
# gained: {"lines": [52, 53, 54, 55, 58, 59, 60, 62, 63, 65, 66, 67, 68, 71, 72, 73, 74, 76, 77, 78, 80, 81, 82, 84, 85, 86, 88, 89, 90, 92, 93, 94, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.cli.vault import VaultCLI
import optparse
import sys

@pytest.fixture
def vault_cli():
    args = MagicMock()
    return VaultCLI(args)

def test_init_parser_create(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'create', 'testfile'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'create'
    assert args.args == ['testfile']

def test_init_parser_decrypt(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'decrypt', 'testfile'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'decrypt'
    assert args.args == ['testfile']

def test_init_parser_edit(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'edit', 'testfile'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'edit'
    assert args.args == ['testfile']

def test_init_parser_view(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'view', 'testfile'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'view'
    assert args.args == ['testfile']

def test_init_parser_encrypt(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'encrypt', 'testfile'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'encrypt'
    assert args.args == ['testfile']

def test_init_parser_encrypt_string(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'encrypt_string', 'sometext'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'encrypt_string'
    assert args.args == ['sometext']

def test_init_parser_rekey(vault_cli, monkeypatch):
    monkeypatch.setattr(sys, 'argv', ['ansible-vault', 'rekey', 'testfile'])
    vault_cli.init_parser()
    args = vault_cli.parser.parse_args()
    assert args.action == 'rekey'
    assert args.args == ['testfile']
