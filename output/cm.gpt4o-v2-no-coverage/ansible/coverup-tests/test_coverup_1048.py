# file: lib/ansible/parsing/yaml/objects.py:342-343
# asked: {"lines": [342, 343], "branches": []}
# gained: {"lines": [342, 343], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    def test_splitlines(self):
        # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
        ciphertext = "line1\nline2\nline3"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        
        # Mock the data property to return the plaintext
        obj.data = ciphertext
        
        # Test splitlines without keepends
        lines = obj.splitlines()
        assert lines == ["line1", "line2", "line3"]
        
        # Test splitlines with keepends
        lines_keepends = obj.splitlines(keepends=True)
        assert lines_keepends == ["line1\n", "line2\n", "line3"]
