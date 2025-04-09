# file: lib/ansible/parsing/yaml/objects.py:339-340
# asked: {"lines": [339, 340], "branches": []}
# gained: {"lines": [339, 340], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    def test_rsplit(self):
        # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
        ciphertext = "encrypted_data"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        
        # Mock the data property to return a known string
        obj.data = "a,b,c,d"
        
        # Test rsplit without arguments
        result = obj.rsplit()
        assert result == ["a,b,c,d"]
        
        # Test rsplit with separator
        result = obj.rsplit(',')
        assert result == ["a", "b", "c", "d"]
        
        # Test rsplit with separator and maxsplit
        result = obj.rsplit(',', 1)
        assert result == ["a,b,c", "d"]
        
        # Clean up
        del obj
