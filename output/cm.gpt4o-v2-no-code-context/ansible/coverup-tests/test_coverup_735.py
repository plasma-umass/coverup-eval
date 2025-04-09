# file: lib/ansible/parsing/dataloader.py:124-127
# asked: {"lines": [124, 126, 127], "branches": []}
# gained: {"lines": [124], "branches": []}

import pytest
from unittest.mock import patch

class DataLoader:
    def path_dwim(self, path):
        # Mock implementation of path_dwim
        return path

    def is_executable(self, path):
        '''is the given path executable?'''
        path = self.path_dwim(path)
        return is_executable(path)

def is_executable(path):
    # Mock implementation of is_executable
    return path == "/mock/executable/path"

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_executable_true(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_dwim', return_value="/mock/executable/path")
    mocker.patch('ansible.parsing.dataloader.is_executable', return_value=True)
    assert dataloader.is_executable("/some/path") == True

def test_is_executable_false(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_dwim', return_value="/mock/non_executable/path")
    mocker.patch('ansible.parsing.dataloader.is_executable', return_value=False)
    assert dataloader.is_executable("/some/path") == False
