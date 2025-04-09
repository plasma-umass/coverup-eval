# file: lib/ansible/cli/vault.py:262-279
# asked: {"lines": [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279], "branches": [[267, 268], [267, 270], [275, 276], [275, 278]]}
# gained: {"lines": [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279], "branches": [[267, 268], [267, 270], [275, 276], [275, 278]]}

import pytest
from ansible.cli.vault import VaultCLI
from ansible.module_utils._text import to_text

class TestVaultCLI:
    
    @pytest.fixture
    def mock_to_text(self, mocker):
        return mocker.patch('ansible.module_utils._text.to_text', side_effect=lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)
    
    def test_format_ciphertext_yaml_with_name(self, mock_to_text):
        b_ciphertext = b"ciphertext_line1\nciphertext_line2"
        indent = 4
        name = "vault_var"
        
        expected_output = "vault_var: !vault |\n    ciphertext_line1\n    ciphertext_line2"
        
        result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent, name)
        
        assert result == expected_output
    
    def test_format_ciphertext_yaml_without_name(self, mock_to_text):
        b_ciphertext = b"ciphertext_line1\nciphertext_line2"
        indent = 4
        
        expected_output = "!vault |\n    ciphertext_line1\n    ciphertext_line2"
        
        result = VaultCLI.format_ciphertext_yaml(b_ciphertext, indent)
        
        assert result == expected_output
    
    def test_format_ciphertext_yaml_default_indent(self, mock_to_text):
        b_ciphertext = b"ciphertext_line1\nciphertext_line2"
        
        expected_output = "!vault |\n          ciphertext_line1\n          ciphertext_line2"
        
        result = VaultCLI.format_ciphertext_yaml(b_ciphertext)
        
        assert result == expected_output
