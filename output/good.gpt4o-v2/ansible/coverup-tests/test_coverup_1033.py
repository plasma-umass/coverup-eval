# file: lib/ansible/parsing/yaml/objects.py:129-132
# asked: {"lines": [129, 132], "branches": []}
# gained: {"lines": [129, 132], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

def test_reversed_method(monkeypatch):
    # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
    ciphertext = b"encryptedtext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)

    # Mock the __getitem__ method to return the ciphertext in reverse
    def mock_getitem(self, index):
        return obj._ciphertext[::-1][index]

    monkeypatch.setattr(obj, '__getitem__', mock_getitem)

    # Call the __reversed__ method and check the result
    reversed_text = obj.__reversed__()
    assert reversed_text == to_text(ciphertext[::-1], errors='surrogate_or_strict')
