# file: lib/ansible/parsing/yaml/objects.py:152-153
# asked: {"lines": [152, 153], "branches": []}
# gained: {"lines": [152, 153], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "123.45"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("mock_ciphertext")

def test_float_conversion(encrypted_unicode, mocker):
    mock_vault = MockVault()
    mocker.patch.object(encrypted_unicode, 'vault', mock_vault)
    
    result = float(encrypted_unicode)
    
    assert result == 123.45
