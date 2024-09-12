# file: lib/ansible/parsing/yaml/dumper.py:40-41
# asked: {"lines": [40, 41], "branches": []}
# gained: {"lines": [40], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.parsing.yaml.dumper import AnsibleDumper

class CustomDumper(AnsibleDumper):
    def represent_hostvars(self, data):
        return self.represent_dict(dict(data))

class TestAnsibleDumper:
    def test_represent_hostvars(self):
        # Create a mock instance of CustomDumper
        dumper = CustomDumper(None, None, None)
        
        # Mock the represent_dict method
        dumper.represent_dict = MagicMock(return_value='mocked_dict_representation')
        
        # Create a sample data to pass to represent_hostvars
        sample_data = {'key1': 'value1', 'key2': 'value2'}
        
        # Call the represent_hostvars method
        result = dumper.represent_hostvars(sample_data)
        
        # Assert that represent_dict was called with the correct argument
        dumper.represent_dict.assert_called_once_with({'key1': 'value1', 'key2': 'value2'})
        
        # Assert that the result is as expected
        assert result == 'mocked_dict_representation'
