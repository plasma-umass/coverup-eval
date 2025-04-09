# file: lib/ansible/parsing/yaml/objects.py:140-141
# asked: {"lines": [140, 141], "branches": []}
# gained: {"lines": [140, 141], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes, to_text

class MockVault:
    def decrypt(self, ciphertext, obj):
        return ciphertext

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data, vault=None):
        self.vault = vault
        self._ciphertext = to_bytes(data)

    @property
    def data(self):
        if not self.vault:
            return to_text(self._ciphertext)
        return to_text(self.vault.decrypt(self._ciphertext, obj=self))

def test_encode_with_text_data():
    obj = MockAnsibleVaultEncryptedUnicode("test string")
    encoded = obj.encode(encoding="utf-8")
    assert encoded == to_bytes("test string")

def test_encode_with_bytes_data():
    obj = MockAnsibleVaultEncryptedUnicode(b"test bytes")
    encoded = obj.encode(encoding="utf-8")
    assert encoded == b"test bytes"

def test_encode_with_nonstring_data():
    obj = MockAnsibleVaultEncryptedUnicode(12345)
    encoded = obj.encode(encoding="utf-8")
    assert encoded == to_bytes("12345")

def test_encode_with_encoding():
    obj = MockAnsibleVaultEncryptedUnicode("test string")
    encoded = obj.encode(encoding="utf-16")
    assert encoded == to_bytes("test string", encoding="utf-16")

def test_encode_with_errors():
    obj = MockAnsibleVaultEncryptedUnicode("test string")
    encoded = obj.encode(encoding="utf-8", errors="ignore")
    assert encoded == to_bytes("test string", encoding="utf-8", errors="ignore")

def test_encode_with_vault():
    vault = MockVault()
    obj = MockAnsibleVaultEncryptedUnicode("encrypted string", vault=vault)
    encoded = obj.encode(encoding="utf-8")
    assert encoded == to_bytes("encrypted string")
