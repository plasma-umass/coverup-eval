# file lib/ansible/parsing/yaml/dumper.py:40-41
# lines [40, 41]
# branches []

import pytest
from ansible.parsing.yaml.dumper import AnsibleDumper
from unittest.mock import MagicMock
import yaml

class CustomDumper(AnsibleDumper):
    def represent_hostvars(self, data):
        return self.represent_dict(dict(data))

def test_represent_hostvars(mocker):
    # Create a mock for the represent_dict method
    mock_represent_dict = mocker.patch.object(CustomDumper, 'represent_dict', return_value='mocked_result')

    # Create a mock stream to pass to CustomDumper
    mock_stream = MagicMock()

    # Create an instance of CustomDumper with the mock stream
    dumper = CustomDumper(mock_stream)

    # Create a sample data to be passed to represent_hostvars
    sample_data = {'key1': 'value1', 'key2': 'value2'}

    # Call the represent_hostvars method
    result = dumper.represent_hostvars(sample_data)

    # Assert that represent_dict was called with the correct argument
    mock_represent_dict.assert_called_once_with(dict(sample_data))

    # Assert that the result is as expected
    assert result == 'mocked_result'
