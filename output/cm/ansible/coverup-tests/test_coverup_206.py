# file lib/ansible/cli/vault.py:262-279
# lines [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279]
# branches ['267->268', '267->270', '275->276', '275->278']

import pytest
from ansible.cli.vault import VaultCLI
from ansible.module_utils._text import to_bytes

def test_format_ciphertext_yaml_with_name(mocker):
    # Setup
    mocker.patch('ansible.cli.vault.to_text', return_value='ciphertext_line1\nciphertext_line2')

    # Test
    result = VaultCLI.format_ciphertext_yaml(to_bytes('test_ciphertext'), name='test_name')

    # Assertions
    expected_result = "test_name: !vault |\n          ciphertext_line1\n          ciphertext_line2"
    assert result == expected_result

def test_format_ciphertext_yaml_without_name(mocker):
    # Setup
    mocker.patch('ansible.cli.vault.to_text', return_value='ciphertext_line1\nciphertext_line2')

    # Test
    result = VaultCLI.format_ciphertext_yaml(to_bytes('test_ciphertext'))

    # Assertions
    expected_result = "!vault |\n          ciphertext_line1\n          ciphertext_line2"
    assert result == expected_result

def test_format_ciphertext_yaml_with_custom_indent(mocker):
    # Setup
    mocker.patch('ansible.cli.vault.to_text', return_value='ciphertext_line1\nciphertext_line2')

    # Test
    result = VaultCLI.format_ciphertext_yaml(to_bytes('test_ciphertext'), indent=4, name='test_name')

    # Assertions
    expected_result = "test_name: !vault |\n    ciphertext_line1\n    ciphertext_line2"
    assert result == expected_result
