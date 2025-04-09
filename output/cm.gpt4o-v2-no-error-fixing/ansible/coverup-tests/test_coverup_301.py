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
    given = '/absolute/path'
    result = loader.path_dwim(given)
    assert result == unfrackpath(given, follow=False)

def test_path_dwim_home_path(dataloader, monkeypatch):
    loader = dataloader('/mock/basedir')
    given = '~/home/path'
    expanded_path = os.path.expanduser(given)
    monkeypatch.setattr(os.path, 'expanduser', lambda x: expanded_path)
    result = loader.path_dwim(given)
    assert result == unfrackpath(expanded_path, follow=False)

def test_path_dwim_relative_path(dataloader):
    loader = dataloader('/mock/basedir')
    given = 'relative/path'
    expected_path = os.path.join('/mock/basedir', given)
    result = loader.path_dwim(given)
    assert result == unfrackpath(expected_path, follow=False)
