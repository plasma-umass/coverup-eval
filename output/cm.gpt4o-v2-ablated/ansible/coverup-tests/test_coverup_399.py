# file: lib/ansible/parsing/dataloader.py:78-80
# asked: {"lines": [78, 80], "branches": []}
# gained: {"lines": [78, 80], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_vault():
    class MockVault:
        secrets = 'mock_secrets'
    return MockVault()

@pytest.fixture
def dataloader(mock_vault):
    loader = DataLoader()
    loader._vault = mock_vault
    return loader

@patch('ansible.parsing.dataloader.from_yaml')
def test_load_default(mock_from_yaml, dataloader):
    data = 'some_data'
    file_name = '<string>'
    show_content = True
    json_only = False

    dataloader.load(data)

    mock_from_yaml.assert_called_once_with(data, file_name, show_content, 'mock_secrets', json_only=json_only)

@patch('ansible.parsing.dataloader.from_yaml')
def test_load_custom_filename(mock_from_yaml, dataloader):
    data = 'some_data'
    file_name = 'custom_file.yml'
    show_content = True
    json_only = False

    dataloader.load(data, file_name=file_name)

    mock_from_yaml.assert_called_once_with(data, file_name, show_content, 'mock_secrets', json_only=json_only)

@patch('ansible.parsing.dataloader.from_yaml')
def test_load_hide_content(mock_from_yaml, dataloader):
    data = 'some_data'
    file_name = '<string>'
    show_content = False
    json_only = False

    dataloader.load(data, show_content=show_content)

    mock_from_yaml.assert_called_once_with(data, file_name, show_content, 'mock_secrets', json_only=json_only)

@patch('ansible.parsing.dataloader.from_yaml')
def test_load_json_only(mock_from_yaml, dataloader):
    data = 'some_data'
    file_name = '<string>'
    show_content = True
    json_only = True

    dataloader.load(data, json_only=json_only)

    mock_from_yaml.assert_called_once_with(data, file_name, show_content, 'mock_secrets', json_only=json_only)
