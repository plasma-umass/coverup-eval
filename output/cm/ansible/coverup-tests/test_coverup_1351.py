# file lib/ansible/plugins/loader.py:102-106
# lines [104, 105, 106]
# branches ['105->exit', '105->106']

import pytest
import sys
from ansible.plugins.loader import add_dirs_to_loader

# Mock loader class to test add_dirs_to_loader function
class MockLoader:
    def __init__(self):
        self.directories = []

    def add_directory(self, path, with_subdir):
        self.directories.append((path, with_subdir))

@pytest.fixture
def mock_loader(mocker):
    # Create a mock loader and patch it into the sys.modules
    mock_loader = MockLoader()
    module_name = 'ansible.plugins.loader'
    loader_name = 'test_loader'
    full_loader_name = f'{module_name}.{loader_name}'
    mocker.patch.dict(sys.modules, {full_loader_name: mock_loader})
    return mock_loader

def test_add_dirs_to_loader(mock_loader, mocker):
    paths = ['/path/to/dir1', '/path/to/dir2']
    # Patch the getattr to return our mock_loader when the specific loader is requested
    mocker.patch('ansible.plugins.loader.getattr', return_value=mock_loader)
    add_dirs_to_loader('test', paths)
    assert len(mock_loader.directories) == 2
    assert mock_loader.directories[0] == ('/path/to/dir1', True)
    assert mock_loader.directories[1] == ('/path/to/dir2', True)
