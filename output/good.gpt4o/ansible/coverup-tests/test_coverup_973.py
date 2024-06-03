# file lib/ansible/parsing/yaml/objects.py:152-153
# lines [152, 153]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleBaseYAMLObject:
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        if not self.vault:
            raise AttributeError("Vault attribute is missing")
        return self._data

class MockSequence:
    pass

class TestAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject, AnsibleVaultEncryptedUnicode):
    pass

def test_ansible_vault_encrypted_unicode_float():
    # Create an instance with a float-convertible string
    obj = TestAnsibleVaultEncryptedUnicode("123.45")
    
    # Assert that the float conversion is correct
    assert float(obj) == 123.45

    # Create an instance with a non-float-convertible string to test exception
    obj_invalid = TestAnsibleVaultEncryptedUnicode("invalid_float")
    
    with pytest.raises(ValueError):
        float(obj_invalid)
