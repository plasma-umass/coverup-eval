# file: lib/ansible/cli/vault.py:385-417
# asked: {"lines": [388, 389, 390, 393, 398, 400, 402, 403, 406, 408, 409, 410, 411, 412, 414, 415, 417], "branches": [[389, 390], [389, 393], [398, 400], [398, 417], [409, 410], [409, 415], [411, 412], [411, 414]]}
# gained: {"lines": [388, 389, 390, 393, 398, 400, 402, 403, 406, 408, 409, 410, 411, 412, 414, 415, 417], "branches": [[389, 390], [389, 393], [398, 400], [398, 417], [409, 410], [409, 415], [411, 412], [411, 414]]}

import pytest
from ansible.cli.vault import VaultCLI
from unittest.mock import MagicMock

@pytest.fixture
def vault_cli():
    cli = VaultCLI(args=['dummy_arg'])
    cli.editor = MagicMock()
    cli.encrypt_secret = b'secret'
    cli.editor.encrypt_bytes = MagicMock(return_value=b'encrypted_data')
    cli.format_ciphertext_yaml = MagicMock(return_value='yaml_text')
    return cli

def test_format_output_vault_strings_single_item(vault_cli):
    b_plaintext_list = [(b'plaintext', 'source', 'name')]
    result = vault_cli._format_output_vault_strings(b_plaintext_list)
    
    assert len(result) == 1
    assert result[0]['out'] == 'yaml_text'
    assert result[0]['err'] is None

def test_format_output_vault_strings_multiple_items_with_names(vault_cli):
    b_plaintext_list = [
        (b'plaintext1', 'source1', 'name1'),
        (b'plaintext2', 'source2', 'name2')
    ]
    result = vault_cli._format_output_vault_strings(b_plaintext_list)
    
    assert len(result) == 2
    assert result[0]['out'] == 'yaml_text'
    assert result[0]['err'] == '# The encrypted version of variable ("name1", the string #1 from source1).\n'
    assert result[1]['out'] == 'yaml_text'
    assert result[1]['err'] == '# The encrypted version of variable ("name2", the string #2 from source2).\n'

def test_format_output_vault_strings_multiple_items_without_names(vault_cli):
    b_plaintext_list = [
        (b'plaintext1', 'source1', None),
        (b'plaintext2', 'source2', None)
    ]
    result = vault_cli._format_output_vault_strings(b_plaintext_list)
    
    assert len(result) == 2
    assert result[0]['out'] == 'yaml_text'
    assert result[0]['err'] == '# The encrypted version of the string #1 from source1.)\n'
    assert result[1]['out'] == 'yaml_text'
    assert result[1]['err'] == '# The encrypted version of the string #2 from source2.)\n'
