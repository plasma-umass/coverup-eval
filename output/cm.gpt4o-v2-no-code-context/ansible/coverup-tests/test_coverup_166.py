# file: lib/ansible/cli/vault.py:262-279
# asked: {"lines": [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279], "branches": [[267, 268], [267, 270], [275, 276], [275, 278]]}
# gained: {"lines": [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279], "branches": [[267, 268], [267, 270], [275, 276], [275, 278]]}

import pytest
from ansible.cli.vault import VaultCLI

def test_format_ciphertext_yaml_no_name():
    b_ciphertext = b"encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext)
    expected = "!vault |\n          encrypted_data"
    assert result == expected

def test_format_ciphertext_yaml_with_name():
    b_ciphertext = b"encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext, name="secret")
    expected = "secret: !vault |\n          encrypted_data"
    assert result == expected

def test_format_ciphertext_yaml_with_indent():
    b_ciphertext = b"encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent=4)
    expected = "!vault |\n    encrypted_data"
    assert result == expected

def test_format_ciphertext_yaml_with_name_and_indent():
    b_ciphertext = b"encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent=4, name="secret")
    expected = "secret: !vault |\n    encrypted_data"
    assert result == expected
