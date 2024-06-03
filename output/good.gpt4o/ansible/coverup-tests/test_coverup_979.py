# file lib/ansible/parsing/yaml/objects.py:149-150
# lines [149, 150]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_int():
    # Create an instance of the mock class with a valid integer string
    encrypted_unicode = MockAnsibleVaultEncryptedUnicode("12345")
    
    # Test the __int__ method
    result = encrypted_unicode.__int__()
    
    # Assert the result is as expected
    assert result == 12345

    # Create an instance of the mock class with a valid integer string in a different base
    encrypted_unicode_base16 = MockAnsibleVaultEncryptedUnicode("1a")
    
    # Test the __int__ method with base 16
    result_base16 = encrypted_unicode_base16.__int__(base=16)
    
    # Assert the result is as expected
    assert result_base16 == 26

    # Create an instance of the mock class with an invalid integer string
    encrypted_unicode_invalid = MockAnsibleVaultEncryptedUnicode("invalid")
    
    # Test the __int__ method and expect a ValueError
    with pytest.raises(ValueError):
        encrypted_unicode_invalid.__int__()

