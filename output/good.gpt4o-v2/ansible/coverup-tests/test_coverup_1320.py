# file: lib/ansible/parsing/yaml/objects.py:348-349
# asked: {"lines": [349], "branches": []}
# gained: {"lines": [349], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return ciphertext.decode('utf-8')

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self):
        return MockVault().decrypt(self._ciphertext)
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_decrypt))

def test_strip(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode(b"  secret data  ")
    stripped_text = encrypted_text.strip()
    assert stripped_text == "secret data"

def test_strip_with_chars(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode(b"xxsecret dataxx")
    stripped_text = encrypted_text.strip('x')
    assert stripped_text == "secret data"
