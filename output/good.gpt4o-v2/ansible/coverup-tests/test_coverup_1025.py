# file: lib/ansible/parsing/yaml/objects.py:140-141
# asked: {"lines": [140, 141], "branches": []}
# gained: {"lines": [140, 141], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self):
        return "decrypted_data"
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_decrypt))

def test_encode(mock_vault):
    ciphertext = "encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    encoded_data = obj.encode(encoding='utf-8', errors='strict')
    
    assert encoded_data == to_bytes("decrypted_data", encoding='utf-8', errors='strict')
