# file: lib/ansible/cli/vault.py:385-417
# asked: {"lines": [385, 388, 389, 390, 393, 398, 400, 402, 403, 406, 408, 409, 410, 411, 412, 414, 415, 417], "branches": [[389, 390], [389, 393], [398, 400], [398, 417], [409, 410], [409, 415], [411, 412], [411, 414]]}
# gained: {"lines": [385, 388, 389, 390, 393, 398, 400, 402, 403, 406, 408, 409, 410, 411, 412, 414, 415, 417], "branches": [[389, 390], [389, 393], [398, 400], [398, 417], [409, 410], [409, 415], [411, 412], [411, 414]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    args = MagicMock()
    cli = VaultCLI(args)
    cli.editor = MagicMock()
    cli.encrypt_secret = MagicMock()
    return cli

def test_format_output_vault_strings_single_item(vault_cli):
    b_plaintext_list = [(b'secret', 'source', 'var_name')]
    vault_cli.editor.encrypt_bytes.return_value = b'encrypted_secret'
    vault_cli.format_ciphertext_yaml = MagicMock(return_value='var_name: !vault |\n          encrypted_secret')

    result = vault_cli._format_output_vault_strings(b_plaintext_list)

    assert len(result) == 1
    assert result[0]['out'] == 'var_name: !vault |\n          encrypted_secret'
    assert result[0]['err'] is None

def test_format_output_vault_strings_multiple_items(vault_cli):
    b_plaintext_list = [
        (b'secret1', 'source1', 'var_name1'),
        (b'secret2', 'source2', None)
    ]
    vault_cli.editor.encrypt_bytes.side_effect = [b'encrypted_secret1', b'encrypted_secret2']
    vault_cli.format_ciphertext_yaml.side_effect = [
        'var_name1: !vault |\n          encrypted_secret1',
        '!vault |\n          encrypted_secret2'
    ]

    result = vault_cli._format_output_vault_strings(b_plaintext_list)

    assert len(result) == 2
    assert result[0]['out'] == 'var_name1: !vault |\n          encrypted_secret1'
    assert result[0]['err'] == '# The encrypted version of variable ("var_name1", the string #1 from source1).\n'
    assert result[1]['out'] == '!vault |\n          encrypted_secret2'
    assert result[1]['err'] == '# The encrypted version of the string #2 from source2.)\n'
