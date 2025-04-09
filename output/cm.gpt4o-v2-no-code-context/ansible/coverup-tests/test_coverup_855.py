# file: lib/ansible/parsing/yaml/objects.py:129-132
# asked: {"lines": [129, 132], "branches": []}
# gained: {"lines": [129, 132], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

class TestAnsibleVaultEncryptedUnicode:
    
    def test_reversed_method(self):
        # Create a mock object of AnsibleVaultEncryptedUnicode
        class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
            def __init__(self, value):
                self.value = value
            
            def __getitem__(self, index):
                return self.value[index]
            
            def __len__(self):
                return len(self.value)
        
        # Initialize the mock object with a sample string
        sample_string = "encrypted_string"
        mock_obj = MockAnsibleVaultEncryptedUnicode(sample_string)
        
        # Call the __reversed__ method
        reversed_result = mock_obj.__reversed__()
        
        # Verify the result
        expected_result = to_text(sample_string[::-1], errors='surrogate_or_strict')
        assert reversed_result == expected_result
