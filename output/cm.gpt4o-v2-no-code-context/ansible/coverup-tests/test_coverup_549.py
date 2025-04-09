# file: lib/ansible/parsing/yaml/objects.py:165-168
# asked: {"lines": [165, 166, 167, 168], "branches": [[166, 167], [166, 168]]}
# gained: {"lines": [165, 166, 167, 168], "branches": [[166, 167], [166, 168]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute

    @property
    def data(self):
        return self._data

@pytest.fixture
def encrypted_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted_data")

def test_lt_with_same_class(encrypted_unicode):
    other = MockAnsibleVaultEncryptedUnicode("other_encrypted_data")
    assert (encrypted_unicode < other) == (encrypted_unicode.data < other.data)

def test_lt_with_string(encrypted_unicode):
    other = "other_encrypted_data"
    assert (encrypted_unicode < other) == (encrypted_unicode.data < other)
