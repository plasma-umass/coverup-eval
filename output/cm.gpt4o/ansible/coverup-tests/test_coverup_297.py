# file lib/ansible/parsing/dataloader.py:82-106
# lines [82, 85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106]
# branches ['90->91', '90->94', '102->103', '102->106']

import pytest
import json
import yaml
from unittest.mock import patch, mock_open, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._FILE_CACHE = {}
    return loader

def test_load_from_file_cache(dataloader, mocker):
    file_name = 'test_file.json'
    dataloader._FILE_CACHE[file_name] = {'key': 'value'}
    
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_name)
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
    
    result = dataloader.load_from_file(file_name, cache=True)
    
    assert result == {'key': 'value'}

def test_load_from_file_no_cache(dataloader, mocker):
    file_name = 'test_file.json'
    file_content = '{"key": "value"}'
    
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_name)
    mocker.patch('ansible.parsing.dataloader.DataLoader._get_file_contents', return_value=(file_content.encode(), True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value=file_content)
    mocker.patch('ansible.parsing.dataloader.DataLoader.load', return_value=json.loads(file_content))
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
    
    result = dataloader.load_from_file(file_name, cache=False)
    
    assert result == {'key': 'value'}
    assert dataloader._FILE_CACHE[file_name] == {'key': 'value'}

def test_load_from_file_unsafe(dataloader, mocker):
    file_name = 'test_file.json'
    file_content = '{"key": "value"}'
    
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_name)
    mocker.patch('ansible.parsing.dataloader.DataLoader._get_file_contents', return_value=(file_content.encode(), True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value=file_content)
    mocker.patch('ansible.parsing.dataloader.DataLoader.load', return_value=json.loads(file_content))
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
    
    result = dataloader.load_from_file(file_name, cache=False, unsafe=True)
    
    assert result == {'key': 'value'}
    assert dataloader._FILE_CACHE[file_name] == {'key': 'value'}

def test_load_from_file_yaml(dataloader, mocker):
    file_name = 'test_file.yaml'
    file_content = 'key: value'
    
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_name)
    mocker.patch('ansible.parsing.dataloader.DataLoader._get_file_contents', return_value=(file_content.encode(), True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value=file_content)
    mocker.patch('ansible.parsing.dataloader.DataLoader.load', return_value=yaml.safe_load(file_content))
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
    
    result = dataloader.load_from_file(file_name, cache=False)
    
    assert result == {'key': 'value'}
    assert dataloader._FILE_CACHE[file_name] == {'key': 'value'}

def test_load_from_file_not_found(dataloader, mocker):
    file_name = 'non_existent_file.json'
    
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_name)
    mocker.patch('ansible.parsing.dataloader.DataLoader._get_file_contents', side_effect=AnsibleFileNotFound("Unable to retrieve file contents", file_name=file_name))
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=False)
    
    with pytest.raises(AnsibleFileNotFound):
        dataloader.load_from_file(file_name, cache=False)
