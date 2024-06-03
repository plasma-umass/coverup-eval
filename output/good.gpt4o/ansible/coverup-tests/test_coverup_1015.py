# file lib/ansible/parsing/yaml/objects.py:342-343
# lines [342, 343]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mock the vault attribute to avoid AttributeError

    @property
    def data(self):
        return self._data

def test_splitlines():
    # Create an instance of the mock class with sample data
    sample_data = "line1\nline2\nline3"
    obj = MockAnsibleVaultEncryptedUnicode(sample_data)
    
    # Test splitlines without keepends
    result = obj.splitlines()
    assert result == ["line1", "line2", "line3"], f"Expected ['line1', 'line2', 'line3'], but got {result}"
    
    # Test splitlines with keepends
    result_keepends = obj.splitlines(keepends=True)
    assert result_keepends == ["line1\n", "line2\n", "line3"], f"Expected ['line1\\n', 'line2\\n', 'line3'], but got {result_keepends}"
