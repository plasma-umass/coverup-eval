# file lib/ansible/cli/vault.py:262-279
# lines [262, 263, 264, 266, 267, 268, 270, 271, 272, 274, 275, 276, 278, 279]
# branches ['267->268', '267->270', '275->276', '275->278']

import pytest
from ansible.cli.vault import VaultCLI

def test_format_ciphertext_yaml(mocker):
    # Mock the to_text function to return a predictable ciphertext
    mocker.patch('ansible.cli.vault.to_text', return_value="ciphertext_line1\nciphertext_line2")

    # Test with default indent and no name
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext=b"dummy_ciphertext")
    expected_result = "!vault |\n          ciphertext_line1\n          ciphertext_line2"
    assert result == expected_result

    # Test with custom indent and no name
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext=b"dummy_ciphertext", indent=4)
    expected_result = "!vault |\n    ciphertext_line1\n    ciphertext_line2"
    assert result == expected_result

    # Test with default indent and a name
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext=b"dummy_ciphertext", name="my_var")
    expected_result = "my_var: !vault |\n          ciphertext_line1\n          ciphertext_line2"
    assert result == expected_result

    # Test with custom indent and a name
    result = VaultCLI.format_ciphertext_yaml(b_ciphertext=b"dummy_ciphertext", indent=4, name="my_var")
    expected_result = "my_var: !vault |\n    ciphertext_line1\n    ciphertext_line2"
    assert result == expected_result
