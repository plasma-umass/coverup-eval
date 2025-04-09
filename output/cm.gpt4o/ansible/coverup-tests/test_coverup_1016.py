# file lib/ansible/parsing/yaml/objects.py:348-349
# lines [348, 349]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute to avoid AttributeError

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_strip():
    # Create a mock object with some data
    mock_obj = MockAnsibleVaultEncryptedUnicode("  secret_data  ")

    # Test the strip method without arguments
    stripped_data = mock_obj.strip()
    assert stripped_data == "secret_data", f"Expected 'secret_data', got {stripped_data}"

    # Test the strip method with specific characters
    mock_obj._data = "xxsecret_dataxx"
    stripped_data = mock_obj.strip("x")
    assert stripped_data == "secret_data", f"Expected 'secret_data', got {stripped_data}"

    # Test the strip method with different characters
    mock_obj._data = "yysecret_datayy"
    stripped_data = mock_obj.strip("y")
    assert stripped_data == "secret_data", f"Expected 'secret_data', got {stripped_data}"
