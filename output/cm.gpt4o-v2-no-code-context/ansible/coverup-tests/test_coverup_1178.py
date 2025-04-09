# file: lib/ansible/plugins/loader.py:102-106
# asked: {"lines": [104, 105, 106], "branches": [[105, 0], [105, 106]]}
# gained: {"lines": [104, 105, 106], "branches": [[105, 0], [105, 106]]}

import pytest
import sys
from unittest.mock import MagicMock

# Assuming the add_dirs_to_loader function is part of a class or module named LoaderModule
from ansible.plugins.loader import add_dirs_to_loader

@pytest.fixture
def mock_loader(monkeypatch):
    class MockLoader:
        def add_directory(self, path, with_subdir):
            self.path = path
            self.with_subdir = with_subdir

    mock_loader_instance = MockLoader()
    monkeypatch.setattr(sys.modules['ansible.plugins.loader'], 'test_loader', mock_loader_instance)
    return mock_loader_instance

def test_add_dirs_to_loader_single_path(mock_loader):
    paths = ['/test/path']
    add_dirs_to_loader('test', paths)
    assert mock_loader.path == '/test/path'
    assert mock_loader.with_subdir is True

def test_add_dirs_to_loader_multiple_paths(mock_loader):
    paths = ['/test/path1', '/test/path2']
    add_dirs_to_loader('test', paths)
    # Since the loop will overwrite the path, we only check the last one
    assert mock_loader.path == '/test/path2'
    assert mock_loader.with_subdir is True
