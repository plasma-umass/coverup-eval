# file: lib/ansible/parsing/yaml/dumper.py:40-41
# asked: {"lines": [41], "branches": []}
# gained: {"lines": [41], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.parsing.yaml.dumper import AnsibleDumper, represent_hostvars

class TestAnsibleDumper:
    def test_represent_hostvars(self):
        # Create a mock AnsibleDumper instance
        dumper = AnsibleDumper(None)
        
        # Mock the represent_dict method
        dumper.represent_dict = MagicMock(return_value="mocked_result")
        
        # Create a sample data to pass to represent_hostvars
        data = {'key': 'value'}
        
        # Call the represent_hostvars method
        result = represent_hostvars(dumper, data)
        
        # Assert that represent_dict was called with the correct argument
        dumper.represent_dict.assert_called_once_with({'key': 'value'})
        
        # Assert the result is as expected
        assert result == "mocked_result"
