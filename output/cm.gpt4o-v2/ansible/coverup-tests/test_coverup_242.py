# file: lib/ansible/cli/console.py:302-320
# asked: {"lines": [302, 311, 312, 313, 314, 315, 316, 318, 320], "branches": [[311, 312], [311, 313], [313, 314], [313, 315], [315, 316], [315, 318]]}
# gained: {"lines": [302, 311, 312, 313, 314, 315, 316, 318, 320], "branches": [[311, 312], [311, 313], [313, 314], [313, 315], [315, 316], [315, 318]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.console import ConsoleCLI

@pytest.fixture
def console_cli():
    args = ['test']
    cli = ConsoleCLI(args)
    cli.inventory = MagicMock()
    cli.set_prompt = MagicMock()
    return cli

def test_do_cd_no_arg(console_cli):
    console_cli.do_cd('')
    assert console_cli.cwd == '*'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_root(console_cli):
    console_cli.do_cd('/')
    assert console_cli.cwd == 'all'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_valid_host(console_cli):
    console_cli.inventory.get_hosts.return_value = ['host1']
    console_cli.do_cd('host1')
    assert console_cli.cwd == 'host1'
    console_cli.set_prompt.assert_called_once()

def test_do_cd_invalid_host(console_cli, mocker):
    mock_display = mocker.patch('ansible.cli.console.display.display')
    console_cli.inventory.get_hosts.return_value = []
    console_cli.do_cd('invalid_host')
    assert console_cli.cwd != 'invalid_host'
    mock_display.assert_called_once_with("no host matched")
    console_cli.set_prompt.assert_called_once()
