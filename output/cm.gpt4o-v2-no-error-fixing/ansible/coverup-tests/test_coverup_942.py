# file: lib/ansible/parsing/yaml/objects.py:342-343
# asked: {"lines": [343], "branches": []}
# gained: {"lines": [343], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_splitlines():
    ciphertext = "line1\nline2\nline3"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    # Mock the data property to return the ciphertext
    obj.data = ciphertext
    
    # Test splitlines without keepends
    result = obj.splitlines()
    assert result == ["line1", "line2", "line3"]
    
    # Test splitlines with keepends
    result = obj.splitlines(keepends=True)
    assert result == ["line1\n", "line2\n", "line3"]

    # Clean up
    del obj
