# file: lib/ansible/cli/vault.py:385-417
# asked: {"lines": [390, 410, 411, 412, 414], "branches": [[389, 390], [409, 410], [411, 412], [411, 414]]}
# gained: {"lines": [390, 410, 411, 412, 414], "branches": [[389, 390], [409, 410], [411, 412], [411, 414]]}

import pytest
from unittest.mock import MagicMock
from ansible.cli.vault import VaultCLI

@pytest.fixture
def vault_cli():
    cli = VaultCLI(args=['test'])
    cli.editor = MagicMock()
    cli.encrypt_secret = b'secret'
    return cli

def test_format_output_vault_strings_single_item(vault_cli):
    b_plaintext_list = [(b'plaintext', 'source', 'name')]
    vault_cli.editor.encrypt_bytes.return_value = b'ciphertext'
    vault_cli.format_ciphertext_yaml = MagicMock(return_value='name: !vault |\n          ciphertext')

    result = vault_cli._format_output_vault_strings(b_plaintext_list)

    assert len(result) == 1
    assert result[0]['out'] == 'name: !vault |\n          ciphertext'
    assert result[0]['err'] is None

def test_format_output_vault_strings_multiple_items_with_name(vault_cli):
    b_plaintext_list = [
        (b'plaintext1', 'source1', 'name1'),
        (b'plaintext2', 'source2', 'name2')
    ]
    vault_cli.editor.encrypt_bytes.side_effect = [b'ciphertext1', b'ciphertext2']
    vault_cli.format_ciphertext_yaml.side_effect = [
        'name1: !vault |\n          ciphertext1',
        'name2: !vault |\n          ciphertext2'
    ]

    result = vault_cli._format_output_vault_strings(b_plaintext_list)

    assert len(result) == 2
    assert result[0]['out'] == 'name1: !vault |\n          ciphertext1'
    assert result[0]['err'] == '# The encrypted version of variable ("name1", the string #1 from source1).\n'
    assert result[1]['out'] == 'name2: !vault |\n          ciphertext2'
    assert result[1]['err'] == '# The encrypted version of variable ("name2", the string #2 from source2).\n'

def test_format_output_vault_strings_multiple_items_without_name(vault_cli):
    b_plaintext_list = [
        (b'plaintext1', 'source1', None),
        (b'plaintext2', 'source2', None)
    ]
    vault_cli.editor.encrypt_bytes.side_effect = [b'ciphertext1', b'ciphertext2']
    vault_cli.format_ciphertext_yaml.side_effect = [
        '!vault |\n          ciphertext1',
        '!vault |\n          ciphertext2'
    ]

    result = vault_cli._format_output_vault_strings(b_plaintext_list)

    assert len(result) == 2
    assert result[0]['out'] == '!vault |\n          ciphertext1'
    assert result[0]['err'] == '# The encrypted version of the string #1 from source1.)\n'
    assert result[1]['out'] == '!vault |\n          ciphertext2'
    assert result[1]['err'] == '# The encrypted version of the string #2 from source2.)\n'
