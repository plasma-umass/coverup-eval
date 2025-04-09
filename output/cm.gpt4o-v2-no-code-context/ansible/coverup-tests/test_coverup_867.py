# file: lib/ansible/parsing/yaml/objects.py:152-153
# asked: {"lines": [152, 153], "branches": []}
# gained: {"lines": [152, 153], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute to avoid AttributeError

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_float():
    # Create an instance with a float-compatible string
    obj = MockAnsibleVaultEncryptedUnicode("123.45")
    
    # Assert that the float conversion works correctly
    assert float(obj) == 123.45

    # Create an instance with an integer-compatible string
    obj = MockAnsibleVaultEncryptedUnicode("678")
    
    # Assert that the float conversion works correctly
    assert float(obj) == 678.0

    # Create an instance with a string that cannot be converted to float
    obj = MockAnsibleVaultEncryptedUnicode("not_a_number")
    
    # Assert that a ValueError is raised
    with pytest.raises(ValueError):
        float(obj)
