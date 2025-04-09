# file: lib/ansible/parsing/yaml/objects.py:327-328
# asked: {"lines": [327, 328], "branches": []}
# gained: {"lines": [327, 328], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    def test_rjust(self):
        # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
        ciphertext = "encrypted_data"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        
        # Mock the data property to return a known string
        obj.data = "test"
        
        # Call the rjust method and verify the result
        result = obj.rjust(10)
        assert result == "      test"
        
        # Clean up
        del obj
