# file: lib/ansible/parsing/yaml/objects.py:92-104
# asked: {"lines": [92, 100, 103, 104], "branches": []}
# gained: {"lines": [92, 100, 103, 104], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

def test_ansible_vault_encrypted_unicode_init():
    ciphertext = "test_ciphertext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    assert obj.vault is None
    assert obj._ciphertext == to_bytes(ciphertext)
