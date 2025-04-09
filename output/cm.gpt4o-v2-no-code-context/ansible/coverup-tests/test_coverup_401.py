# file: lib/ansible/parsing/yaml/objects.py:312-317
# asked: {"lines": [312, 313, 314, 315, 316, 317], "branches": [[313, 314], [313, 315], [315, 316], [315, 317]]}
# gained: {"lines": [312, 313, 314, 315, 316, 317], "branches": [[313, 314], [313, 315], [315, 316], [315, 317]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

@pytest.fixture
def mock_vault_unicode():
    return MockAnsibleVaultEncryptedUnicode("encrypted data")

def test_replace_with_plain_strings(mock_vault_unicode):
    result = mock_vault_unicode.replace("encrypted", "decrypted")
    assert result == "decrypted data"

def test_replace_with_vault_unicode_old(mock_vault_unicode):
    old = MockAnsibleVaultEncryptedUnicode("encrypted")
    result = mock_vault_unicode.replace(old, "decrypted")
    assert result == "decrypted data"

def test_replace_with_vault_unicode_new(mock_vault_unicode):
    new = MockAnsibleVaultEncryptedUnicode("decrypted")
    result = mock_vault_unicode.replace("encrypted", new)
    assert result == "decrypted data"

def test_replace_with_vault_unicode_both(mock_vault_unicode):
    old = MockAnsibleVaultEncryptedUnicode("encrypted")
    new = MockAnsibleVaultEncryptedUnicode("decrypted")
    result = mock_vault_unicode.replace(old, new)
    assert result == "decrypted data"

def test_replace_with_maxsplit(mock_vault_unicode):
    result = mock_vault_unicode.replace("e", "E", 1)
    assert result == "Encrypted data"
