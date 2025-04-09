# file: lib/ansible/parsing/yaml/objects.py:324-325
# asked: {"lines": [325], "branches": []}
# gained: {"lines": [325], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    def test_rindex(self, monkeypatch):
        # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
        ciphertext = "encrypted_data"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        
        # Mock the data property to return a known string
        monkeypatch.setattr(obj, 'data', "this is some encrypted data")
        
        # Test rindex method
        assert obj.rindex("encrypted") == 13
        assert obj.rindex("data") == 23
        
        # Test rindex with start and end parameters
        assert obj.rindex("is", 0, 10) == 5
        
        # Test rindex with a substring that does not exist
        with pytest.raises(ValueError):
            obj.rindex("not_in_string")
        
        # Clean up
        del obj
