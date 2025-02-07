# file: lib/ansible/parsing/yaml/objects.py:228-229
# asked: {"lines": [228, 229], "branches": []}
# gained: {"lines": [228, 229], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    ciphertext = "mock_ciphertext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_casefold(encrypted_unicode):
    # Ensure the data property returns a string that can be casefolded
    encrypted_unicode._ciphertext = b"MOCK_CIPHERTEXT"
    assert encrypted_unicode.casefold() == "decrypted_data".casefold()
