# file: lib/ansible/parsing/yaml/objects.py:253-254
# asked: {"lines": [253, 254], "branches": []}
# gained: {"lines": [253, 254], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute

    @property
    def data(self):
        return self._data

def test_format_map():
    # Create a mock object with a format string
    mock_obj = MockAnsibleVaultEncryptedUnicode("Hello, {name}!")
    
    # Define the mapping to be used in format_map
    mapping = {"name": "World"}
    
    # Call the format_map method and assert the result
    result = mock_obj.format_map(mapping)
    assert result == "Hello, World!"

    # Clean up
    del mock_obj
