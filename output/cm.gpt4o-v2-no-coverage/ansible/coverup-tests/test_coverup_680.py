# file: lib/ansible/parsing/yaml/objects.py:175-178
# asked: {"lines": [175, 176, 177, 178], "branches": [[176, 177], [176, 178]]}
# gained: {"lines": [175, 176, 177, 178], "branches": [[176, 177], [176, 178]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode(b"encrypted_data")

def test_gt_with_same_type(encrypted_unicode, mocker):
    mock_vault = MockVault()
    encrypted_unicode.vault = mock_vault
    
    other = AnsibleVaultEncryptedUnicode(b"other_encrypted_data")
    other.vault = mock_vault
    
    assert (encrypted_unicode > other) == ("decrypted_data" > "decrypted_data")

def test_gt_with_string(encrypted_unicode, mocker):
    mock_vault = MockVault()
    encrypted_unicode.vault = mock_vault
    
    assert (encrypted_unicode > "plain_string") == ("decrypted_data" > "plain_string")
