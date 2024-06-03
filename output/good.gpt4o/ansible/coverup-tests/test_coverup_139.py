# file lib/ansible/plugins/loader.py:421-450
# lines [421, 422, 423, 424, 427, 429, 430, 431, 434, 436, 437, 442, 443, 445, 446, 447, 449, 450]
# branches ['423->424', '423->427', '436->437', '436->442', '442->443', '442->445', '447->449', '447->450']

import pytest
from unittest.mock import MagicMock, patch

# Assuming the PluginLoader class is imported from ansible.plugins.loader
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def mock_acr():
    mock = MagicMock()
    mock.n_python_collection_package_name = 'test_collection'
    mock.subdirs = 'subdir'
    mock.resource = 'resource'
    return mock

@pytest.fixture
def mock_collection_pkg():
    mock = MagicMock()
    mock._collection_meta = {
        'plugin_routing': {
            'plugin_type': {
                'subdir.resource.extension': 'entry_value',
                'subdir.resource': 'entry_value_no_extension'
            }
        }
    }
    return mock

@pytest.fixture
def plugin_loader():
    return PluginLoader('class_name', 'package', 'config', 'subdir')

def test_query_collection_routing_meta_with_extension(plugin_loader, mock_acr, mock_collection_pkg):
    plugin_type = 'plugin_type'
    extension = '.extension'

    with patch('ansible.plugins.loader.import_module') as mock_import_module:
        mock_import_module.side_effect = [mock_collection_pkg, None]
        
        result = plugin_loader._query_collection_routing_meta(mock_acr, plugin_type, extension)
        
        assert result == 'entry_value'
        mock_import_module.assert_any_call('test_collection')
        mock_import_module.assert_any_call('test_collection.plugins.plugin_type')

def test_query_collection_routing_meta_without_extension(plugin_loader, mock_acr, mock_collection_pkg):
    plugin_type = 'plugin_type'
    extension = ''

    with patch('ansible.plugins.loader.import_module') as mock_import_module:
        mock_import_module.side_effect = [mock_collection_pkg, None]
        
        result = plugin_loader._query_collection_routing_meta(mock_acr, plugin_type, extension)
        
        assert result == 'entry_value_no_extension'
        mock_import_module.assert_any_call('test_collection')
        mock_import_module.assert_any_call('test_collection.plugins.plugin_type')

def test_query_collection_routing_meta_no_collection_pkg(plugin_loader, mock_acr):
    plugin_type = 'plugin_type'
    extension = '.extension'

    with patch('ansible.plugins.loader.import_module', return_value=None):
        result = plugin_loader._query_collection_routing_meta(mock_acr, plugin_type, extension)
        
        assert result is None

def test_query_collection_routing_meta_no_collection_meta(plugin_loader, mock_acr):
    plugin_type = 'plugin_type'
    extension = '.extension'

    mock_collection_pkg = MagicMock()
    mock_collection_pkg._collection_meta = None

    with patch('ansible.plugins.loader.import_module', return_value=mock_collection_pkg):
        result = plugin_loader._query_collection_routing_meta(mock_acr, plugin_type, extension)
        
        assert result is None
