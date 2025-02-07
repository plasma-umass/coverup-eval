# file: lib/ansible/plugins/loader.py:102-106
# asked: {"lines": [104, 105, 106], "branches": [[105, 0], [105, 106]]}
# gained: {"lines": [104, 105, 106], "branches": [[105, 0], [105, 106]]}

import pytest
import sys
from ansible.plugins.loader import add_dirs_to_loader, test_loader

class MockLoader:
    def __init__(self):
        self.directories = []

    def add_directory(self, path, with_subdir):
        self.directories.append((path, with_subdir))

@pytest.fixture
def mock_loader(monkeypatch):
    loader = MockLoader()
    monkeypatch.setattr(sys.modules['ansible.plugins.loader'], 'test_loader', loader)
    return loader

def test_add_dirs_to_loader(mock_loader):
    paths = ['/path/one', '/path/two']
    add_dirs_to_loader('test', paths)

    assert len(mock_loader.directories) == 2
    assert mock_loader.directories[0] == ('/path/one', True)
    assert mock_loader.directories[1] == ('/path/two', True)
