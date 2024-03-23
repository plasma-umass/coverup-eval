# file lib/ansible/cli/vault.py:385-417
# lines [385, 388, 389, 390, 393, 398, 400, 402, 403, 406, 408, 409, 410, 411, 412, 414, 415, 417]
# branches ['389->390', '389->393', '398->400', '398->417', '409->410', '409->415', '411->412', '411->414']

import pytest
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli(mocker):
    mocker.patch('ansible.cli.vault.CLI.__init__', return_value=None)
    mocker.patch('ansible.cli.vault.VaultEditor.encrypt_bytes', return_value=b'encrypted')
    mocker.patch('ansible.cli.vault.VaultCLI.format_ciphertext_yaml', return_value='formatted_yaml')
    vault_cli = VaultCLI(args=[])
    vault_cli.editor = mocker.MagicMock()
    vault_cli.encrypt_secret = mocker.MagicMock()
    return vault_cli

def test_format_output_vault_strings_single_item(vault_cli):
    b_plaintext_list = [(b'secret', 'source', 'name')]
    output = vault_cli._format_output_vault_strings(b_plaintext_list)
    assert len(output) == 1
    assert output[0]['out'] == 'formatted_yaml'
    assert output[0]['err'] is None

def test_format_output_vault_strings_multiple_items(vault_cli):
    b_plaintext_list = [(b'secret1', 'source1', 'name1'), (b'secret2', 'source2', None)]
    output = vault_cli._format_output_vault_strings(b_plaintext_list)
    assert len(output) == 2
    assert output[0]['out'] == 'formatted_yaml'
    assert output[0]['err'] == '# The encrypted version of variable ("name1", the string #1 from source1).\n'
    assert output[1]['out'] == 'formatted_yaml'
    assert output[1]['err'] == '# The encrypted version of the string #2 from source2.)\n'
