# file: lib/ansible/parsing/yaml/objects.py:295-296
# asked: {"lines": [295, 296], "branches": []}
# gained: {"lines": [295, 296], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_join(encrypted_unicode, monkeypatch):
    # Mock the data property to return a known value
    monkeypatch.setattr(encrypted_unicode, 'data', 'mock_data')
    
    # Test the join method
    result = encrypted_unicode.join(['a', 'b', 'c'])
    
    # Verify the result
    assert result == 'mock_data'.join(['a', 'b', 'c'])
