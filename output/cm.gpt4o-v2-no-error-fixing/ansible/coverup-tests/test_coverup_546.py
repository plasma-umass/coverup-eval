# file: lib/ansible/parsing/yaml/objects.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

def test_data_setter():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    new_value = "new_ciphertext"
    obj.data = new_value
    assert obj._ciphertext == to_bytes(new_value)
