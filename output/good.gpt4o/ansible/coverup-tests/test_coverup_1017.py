# file lib/ansible/parsing/yaml/objects.py:324-325
# lines [324, 325]
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

def test_ansible_vault_encrypted_unicode_rindex():
    # Create a mock object with some data
    mock_data = "This is a test string with test substring"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    # Test rindex method
    sub = "test"
    start = 0
    end = len(mock_data)
    
    # Expected index of the last occurrence of 'test'
    expected_index = mock_data.rindex(sub, start, end)
    
    # Assert that the rindex method returns the correct index
    assert obj.rindex(sub, start, end) == expected_index

    # Test rindex with different start and end
    start = 10
    end = 30
    expected_index = mock_data.rindex(sub, start, end)
    assert obj.rindex(sub, start, end) == expected_index

    # Test rindex with a substring that does not exist
    sub = "notfound"
    with pytest.raises(ValueError):
        obj.rindex(sub)

    # Test rindex with start and end that do not include the substring
    sub = "test"
    start = 0
    end = 10
    with pytest.raises(ValueError):
        obj.rindex(sub, start, end)
