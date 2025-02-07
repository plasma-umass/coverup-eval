# file: lib/ansible/parsing/yaml/objects.py:165-168
# asked: {"lines": [165, 166, 167, 168], "branches": [[166, 167], [166, 168]]}
# gained: {"lines": [165, 166, 167, 168], "branches": [[166, 167], [166, 168]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_lt_with_same_class(encrypted_unicode):
    other = AnsibleVaultEncryptedUnicode("other_ciphertext")
    other.vault = MockVault()
    assert (encrypted_unicode < other) == ("decrypted_data" < "decrypted_data")

def test_lt_with_string(encrypted_unicode):
    assert (encrypted_unicode < "some_string") == ("decrypted_data" < "some_string")
