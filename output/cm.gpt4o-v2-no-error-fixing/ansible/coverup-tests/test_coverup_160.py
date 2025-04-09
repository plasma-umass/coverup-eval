# file: lib/ansible/parsing/dataloader.py:82-106
# asked: {"lines": [82, 85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106], "branches": [[90, 91], [90, 94], [102, 103], [102, 106]]}
# gained: {"lines": [82, 85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106], "branches": [[90, 91], [90, 94], [102, 103], [102, 106]]}

import pytest
from unittest.mock import patch, mock_open
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError

@pytest.fixture
def dataloader():
    return DataLoader()

def test_load_from_file_cache_hit(dataloader, mocker):
    mocker.patch.object(dataloader, '_FILE_CACHE', {'test_file': 'cached_data'})
    mocker.patch.object(dataloader, 'path_dwim', return_value='test_file')
    
    result = dataloader.load_from_file('test_file')
    
    assert result == 'cached_data'

def test_load_from_file_no_cache(dataloader, mocker):
    mocker.patch.object(dataloader, '_FILE_CACHE', {})
    mocker.patch.object(dataloader, 'path_dwim', return_value='test_file')
    mocker.patch.object(dataloader, '_get_file_contents', return_value=(b'file_data', True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value='file_data')
    mocker.patch.object(dataloader, 'load', return_value='parsed_data')
    
    result = dataloader.load_from_file('test_file')
    
    assert result == 'parsed_data'
    assert dataloader._FILE_CACHE['test_file'] == 'parsed_data'

def test_load_from_file_unsafe(dataloader, mocker):
    mocker.patch.object(dataloader, '_FILE_CACHE', {})
    mocker.patch.object(dataloader, 'path_dwim', return_value='test_file')
    mocker.patch.object(dataloader, '_get_file_contents', return_value=(b'file_data', True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value='file_data')
    mocker.patch.object(dataloader, 'load', return_value='parsed_data')
    
    result = dataloader.load_from_file('test_file', unsafe=True)
    
    assert result == 'parsed_data'

def test_load_from_file_deepcopy(dataloader, mocker):
    mocker.patch.object(dataloader, '_FILE_CACHE', {})
    mocker.patch.object(dataloader, 'path_dwim', return_value='test_file')
    mocker.patch.object(dataloader, '_get_file_contents', return_value=(b'file_data', True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value='file_data')
    mocker.patch.object(dataloader, 'load', return_value={'key': 'value'})
    mocker.patch('copy.deepcopy', return_value={'key': 'value'})
    
    result = dataloader.load_from_file('test_file')
    
    assert result == {'key': 'value'}
    assert result is not dataloader._FILE_CACHE['test_file']
