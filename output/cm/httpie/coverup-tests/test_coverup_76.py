# file httpie/cli/requestitems.py:128-131
# lines [128, 129, 130, 131]
# branches []

import pytest
from httpie.cli.requestitems import KeyValueArg, process_data_embed_raw_json_file_arg
from typing import Dict
import json
import os

# Mocking the load_text_file and load_json functions
def test_process_data_embed_raw_json_file_arg(mocker):
    # Arrange
    test_file_path = 'test.json'
    test_data: Dict[str, str] = {'key': 'value'}
    test_json_content = json.dumps(test_data)
    test_key_value_arg = KeyValueArg(key='test', value=test_file_path, sep='=', orig='test=@test.json')

    # Create a temporary JSON file
    with open(test_file_path, 'w') as f:
        f.write(test_json_content)

    # Mock the load_text_file and load_json functions
    mocker.patch(
        'httpie.cli.requestitems.load_text_file',
        return_value=test_json_content
    )
    mocker.patch(
        'httpie.cli.requestitems.load_json',
        return_value=test_data
    )

    # Act
    result = process_data_embed_raw_json_file_arg(test_key_value_arg)

    # Assert
    assert result == test_data

    # Cleanup
    os.remove(test_file_path)

# Register the test function for pytest
def pytest_configure(config):
    config.pluginmanager.import_plugin("pytest_mock")
