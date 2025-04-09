# file lib/ansible/cli/vault.py:445-455
# lines [445, 448, 454, 455]
# branches ['448->exit', '448->454']

import pytest
from ansible.cli.vault import VaultCLI
from ansible.utils.display import Display
from unittest.mock import MagicMock, patch

@pytest.fixture
def vault_cli(mocker):
    mocker.patch('ansible.context.CLIARGS', {'args': ['fake_vault_file']})
    mocker.patch('ansible.cli.vault.VaultEditor', return_value=MagicMock(plaintext=MagicMock(return_value=b'fake content')))
    mocker.patch('ansible.cli.vault.to_text', return_value='fake content')
    mocker.patch('ansible.cli.vault.VaultCLI.pager')
    with patch('ansible.cli.vault.CLI.__init__', return_value=None):
        vault_cli = VaultCLI(args=[])
    vault_cli.editor = mocker.MagicMock()
    vault_cli.editor.plaintext.return_value = b'fake content'
    vault_cli.display = Display()
    return vault_cli

def test_execute_view(vault_cli, mocker):
    mocker.spy(vault_cli, 'pager')
    vault_cli.execute_view()
    vault_cli.pager.assert_called_once_with('fake content')
    assert vault_cli.pager.call_args[0][0] == 'fake content', "The pager should be called with the decrypted content"
