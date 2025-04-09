# file lib/ansible/parsing/yaml/objects.py:155-156
# lines [155, 156]
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

def test_ansible_vault_encrypted_unicode_complex():
    # Create an instance of the mock class with a valid complex number string
    encrypted_unicode = MockAnsibleVaultEncryptedUnicode("1+2j")
    
    # Verify that the __complex__ method returns the correct complex number
    assert complex(encrypted_unicode) == complex("1+2j")
    
    # Create an instance of the mock class with an invalid complex number string
    encrypted_unicode_invalid = MockAnsibleVaultEncryptedUnicode("invalid")
    
    # Verify that the __complex__ method raises a ValueError for invalid complex number string
    with pytest.raises(ValueError):
        complex(encrypted_unicode_invalid)
