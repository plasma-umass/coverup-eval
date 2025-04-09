# file: lib/ansible/cli/vault.py:262-279
# asked: {"lines": [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279], "branches": [[267, 268], [267, 270], [275, 276], [275, 278]]}
# gained: {"lines": [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279], "branches": [[267, 268], [267, 270], [275, 276], [275, 278]]}

import pytest
from ansible.cli.vault import VaultCLI

def test_format_ciphertext_yaml_with_name():
    b_ciphertext = b"encrypted_data"
    indent = 4
    name = "vault_var"
    
    expected_output = "vault_var: !vault |\n    encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent, name)
    
    assert result == expected_output

def test_format_ciphertext_yaml_without_name():
    b_ciphertext = b"encrypted_data"
    indent = 4
    
    expected_output = "!vault |\n    encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent)
    
    assert result == expected_output

def test_format_ciphertext_yaml_default_indent():
    b_ciphertext = b"encrypted_data"
    
    expected_output = "!vault |\n          encrypted_data"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext)
    
    assert result == expected_output

def test_format_ciphertext_yaml_multiline():
    b_ciphertext = b"line1\nline2\nline3"
    indent = 4
    name = "vault_var"
    
    expected_output = "vault_var: !vault |\n    line1\n    line2\n    line3"
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent, name)
    
    assert result == expected_output
