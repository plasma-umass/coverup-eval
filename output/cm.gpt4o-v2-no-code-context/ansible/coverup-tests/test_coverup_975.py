# file: lib/ansible/parsing/dataloader.py:82-106
# asked: {"lines": [85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106], "branches": [[90, 91], [90, 94], [102, 103], [102, 106]]}
# gained: {"lines": [85, 86, 90, 91, 94, 96, 97, 100, 102, 103, 106], "branches": [[90, 91], [90, 94], [102, 103], [102, 106]]}

import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
import copy

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._FILE_CACHE = {}
    return loader

def test_load_from_file_cache_hit(dataloader, mocker):
    file_name = 'test_file.yml'
    cached_data = {'key': 'value'}
    dataloader._FILE_CACHE[file_name] = cached_data

    mocker.patch.object(dataloader, 'path_dwim', return_value=file_name)
    mocker.patch('ansible.utils.display.Display.debug')

    result = dataloader.load_from_file(file_name, cache=True)

    assert result == copy.deepcopy(cached_data)

def test_load_from_file_no_cache(dataloader, mocker):
    file_name = 'test_file.yml'
    file_content = b'{"key": "value"}'
    parsed_data = {'key': 'value'}

    mocker.patch.object(dataloader, 'path_dwim', return_value=file_name)
    mocker.patch('ansible.utils.display.Display.debug')
    mocker.patch.object(dataloader, '_get_file_contents', return_value=(file_content, True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value=file_content.decode())
    mocker.patch.object(dataloader, 'load', return_value=parsed_data)

    result = dataloader.load_from_file(file_name, cache=True)

    assert result == copy.deepcopy(parsed_data)
    assert dataloader._FILE_CACHE[file_name] == parsed_data

def test_load_from_file_unsafe(dataloader, mocker):
    file_name = 'test_file.yml'
    file_content = b'{"key": "value"}'
    parsed_data = {'key': 'value'}

    mocker.patch.object(dataloader, 'path_dwim', return_value=file_name)
    mocker.patch('ansible.utils.display.Display.debug')
    mocker.patch.object(dataloader, '_get_file_contents', return_value=(file_content, True))
    mocker.patch('ansible.parsing.dataloader.to_text', return_value=file_content.decode())
    mocker.patch.object(dataloader, 'load', return_value=parsed_data)

    result = dataloader.load_from_file(file_name, cache=True, unsafe=True)

    assert result == parsed_data
    assert dataloader._FILE_CACHE[file_name] == parsed_data
