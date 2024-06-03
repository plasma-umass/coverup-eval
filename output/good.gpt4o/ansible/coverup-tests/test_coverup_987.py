# file lib/ansible/parsing/yaml/objects.py:242-243
# lines [242, 243]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute

    @property
    def data(self):
        return self._data

def test_expandtabs():
    mock_data = "a\tb\tc"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    # Test with default tabsize
    result = obj.expandtabs()
    assert result == "a       b       c", f"Expected 'a       b       c', got {result}"
    
    # Test with custom tabsize
    result = obj.expandtabs(4)
    assert result == "a   b   c", f"Expected 'a   b   c', got {result}"
