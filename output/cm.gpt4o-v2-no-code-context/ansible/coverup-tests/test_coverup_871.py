# file: lib/ansible/parsing/dataloader.py:78-80
# asked: {"lines": [78, 80], "branches": []}
# gained: {"lines": [78, 80], "branches": []}

import pytest
from ansible.parsing.dataloader import DataLoader

class MockVault:
    secrets = 'mock_secrets'

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = MockVault()
    return loader

def test_load_yaml(mocker, dataloader):
    mock_from_yaml = mocker.patch('ansible.parsing.dataloader.from_yaml', return_value='mock_result')
    data = 'mock_data'
    file_name = 'mock_file.yml'
    show_content = True
    json_only = False

    result = dataloader.load(data, file_name, show_content, json_only)

    mock_from_yaml.assert_called_once_with(data, file_name, show_content, 'mock_secrets', json_only=json_only)
    assert result == 'mock_result'
