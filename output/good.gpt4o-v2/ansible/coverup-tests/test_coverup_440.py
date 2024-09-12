# file: lib/ansible/parsing/dataloader.py:181-195
# asked: {"lines": [181, 186, 187, 189, 190, 192, 193, 195], "branches": [[189, 190], [189, 192]]}
# gained: {"lines": [181, 186, 187, 189, 190, 192, 193, 195], "branches": [[189, 190], [189, 192]]}

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.utils.path import unfrackpath

@pytest.fixture
def dataloader():
    class MockDataLoader(DataLoader):
        def __init__(self, basedir):
            self._basedir = basedir
    return MockDataLoader

def test_path_dwim_absolute_path(dataloader):
    loader = dataloader('/mock/basedir')
    result = loader.path_dwim('/absolute/path')
    assert result == unfrackpath('/absolute/path', follow=False)

def test_path_dwim_home_path(dataloader, monkeypatch):
    home_path = os.path.expanduser('~')
    loader = dataloader('/mock/basedir')
    result = loader.path_dwim('~/home/path')
    assert result == unfrackpath('~/home/path', follow=False)

def test_path_dwim_relative_path(dataloader):
    loader = dataloader('/mock/basedir')
    result = loader.path_dwim('relative/path')
    assert result == unfrackpath('/mock/basedir/relative/path', follow=False)

def test_path_dwim_with_quotes(dataloader):
    loader = dataloader('/mock/basedir')
    result = loader.path_dwim('"relative/path"')
    assert result == unfrackpath('/mock/basedir/relative/path', follow=False)
