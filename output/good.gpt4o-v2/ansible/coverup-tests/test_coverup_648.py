# file: lib/ansible/parsing/yaml/objects.py:175-178
# asked: {"lines": [175, 176, 177, 178], "branches": [[176, 177], [176, 178]]}
# gained: {"lines": [175, 176, 177, 178], "branches": [[176, 177], [176, 178]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_init(self, ciphertext):
        self.vault = MockVault()
        self._ciphertext = ciphertext
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, '__init__', mock_init)

def test_gt_with_same_class(mock_vault):
    obj1 = AnsibleVaultEncryptedUnicode("ciphertext1")
    obj2 = AnsibleVaultEncryptedUnicode("ciphertext2")
    obj1._ciphertext = b"data1"
    obj2._ciphertext = b"data2"
    assert (obj1 > obj2) == ("data1" > "data2")

def test_gt_with_string(mock_vault):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj._ciphertext = b"data"
    assert (obj > "another_data") == ("data" > "another_data")
