# file lib/ansible/cli/vault.py:385-417
# lines [385, 388, 389, 390, 393, 398, 400, 402, 403, 406, 408, 409, 410, 411, 412, 414, 415, 417]
# branches ['389->390', '389->393', '398->400', '398->417', '409->410', '409->415', '411->412', '411->414']

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli(mocker):
    args = MagicMock()
    cli = VaultCLI(args)
    cli.editor = MagicMock()
    cli.encrypt_secret = 'dummy_secret'
    cli.editor.encrypt_bytes = mocker.Mock(return_value=b'encrypted_data')
    cli.format_ciphertext_yaml = mocker.Mock(return_value='yaml_formatted_data')
    return cli

def test_format_output_vault_strings_single_item(vault_cli):
    b_plaintext_list = [(b'plaintext_data', 'source1', 'var1')]
    result = vault_cli._format_output_vault_strings(b_plaintext_list)
    
    assert len(result) == 1
    assert result[0]['out'] == 'yaml_formatted_data'
    assert result[0]['err'] is None

def test_format_output_vault_strings_multiple_items(vault_cli):
    b_plaintext_list = [
        (b'plaintext_data1', 'source1', 'var1'),
        (b'plaintext_data2', 'source2', 'var2')
    ]
    result = vault_cli._format_output_vault_strings(b_plaintext_list)
    
    assert len(result) == 2
    assert result[0]['out'] == 'yaml_formatted_data'
    assert result[0]['err'] == '# The encrypted version of variable ("var1", the string #1 from source1).\n'
    assert result[1]['out'] == 'yaml_formatted_data'
    assert result[1]['err'] == '# The encrypted version of variable ("var2", the string #2 from source2).\n'
