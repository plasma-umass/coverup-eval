# file lib/ansible/plugins/loader.py:384-388
# lines [384, 387, 388]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the PluginLoader class is imported from ansible.plugins.loader
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def mock_plugin_loader(mocker):
    # Mock the __init__ method to avoid needing the required arguments
    mocker.patch.object(PluginLoader, '__init__', lambda self, class_name, package, config, subdir: None)
    loader = PluginLoader('class_name', 'package', 'config', 'subdir')
    mocker.patch.object(loader, '_get_paths_with_context', return_value=[
        MagicMock(path='/fake/path/one'),
        MagicMock(path='/fake/path/two')
    ])
    return loader

def test_get_paths(mock_plugin_loader):
    paths = mock_plugin_loader._get_paths()
    assert paths == ['/fake/path/one', '/fake/path/two']

    # Ensure _get_paths_with_context was called with the correct argument
    mock_plugin_loader._get_paths_with_context.assert_called_once_with(subdirs=True)

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
