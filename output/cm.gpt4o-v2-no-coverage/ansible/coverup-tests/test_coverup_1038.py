# file: lib/ansible/parsing/yaml/objects.py:218-219
# asked: {"lines": [218, 219], "branches": []}
# gained: {"lines": [218, 219], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("encrypted_data")

def test_mod_operator(encrypted_unicode, monkeypatch):
    monkeypatch.setattr(encrypted_unicode.__class__, 'data', property(lambda self: "decrypted %s"))
    result = encrypted_unicode % "data"
    assert result == "decrypted data"

def test_mod_operator_with_multiple_args(encrypted_unicode, monkeypatch):
    monkeypatch.setattr(encrypted_unicode.__class__, 'data', property(lambda self: "decrypted %s %s"))
    result = encrypted_unicode % ("data1", "data2")
    assert result == "decrypted data1 data2"
