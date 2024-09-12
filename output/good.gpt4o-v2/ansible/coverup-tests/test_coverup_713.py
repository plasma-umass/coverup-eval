# file: lib/ansible/parsing/yaml/objects.py:92-104
# asked: {"lines": [92, 100, 103, 104], "branches": []}
# gained: {"lines": [92, 100, 103, 104], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

def test_ansible_vault_encrypted_unicode_init():
    # Test with a simple string
    ciphertext = "simple string"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert obj.vault is None
    assert obj._ciphertext == to_bytes(ciphertext)

    # Test with bytes input
    ciphertext = b"byte string"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert obj.vault is None
    assert obj._ciphertext == to_bytes(ciphertext)

    # Test with non-string input
    ciphertext = 12345
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert obj.vault is None
    assert obj._ciphertext == to_bytes(str(ciphertext))

    # Test with unicode input
    ciphertext = u"unicode string"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert obj.vault is None
    assert obj._ciphertext == to_bytes(ciphertext)
