# file: lib/ansible/parsing/yaml/objects.py:351-352
# asked: {"lines": [351, 352], "branches": []}
# gained: {"lines": [351, 352], "branches": []}

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

def test_swapcase(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode(b'someEncryptedText')
    encrypted_text.vault = MockVault()
    result = encrypted_text.swapcase()
    assert result == 'SOMEeNCRYPTEDtEXT'
