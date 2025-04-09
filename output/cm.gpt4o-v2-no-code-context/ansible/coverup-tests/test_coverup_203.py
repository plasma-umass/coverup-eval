# file: lib/ansible/plugins/loader.py:390-405
# asked: {"lines": [390, 394, 395, 398, 399, 400, 401, 403, 404, 405], "branches": [[394, 0], [394, 395], [398, 0], [398, 399], [400, 401], [400, 403], [403, 0], [403, 404]]}
# gained: {"lines": [390, 394, 395, 398, 399, 400, 401, 403, 404, 405], "branches": [[394, 0], [394, 395], [398, 0], [398, 399], [400, 401], [400, 403], [403, 0], [403, 404]]}

import pytest
from unittest.mock import MagicMock, patch

# Assuming the PluginLoader class is imported from ansible.plugins.loader
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name=None, package=None, config=None, subdir=None)

def test_load_config_defs_no_class_name(plugin_loader):
    plugin_loader.class_name = None
    plugin_loader._load_config_defs('test_name', MagicMock(), 'test_path')
    # No assertions needed as we are testing non-execution of code

@patch('ansible.plugins.loader.get_plugin_class')
@patch('ansible.plugins.loader.AnsibleLoader')
@patch('ansible.plugins.loader.add_fragments')
@patch('ansible.plugins.loader.C')
@patch('ansible.plugins.loader.display')
def test_load_config_defs_with_class_name(mock_display, mock_C, mock_add_fragments, mock_AnsibleLoader, mock_get_plugin_class, plugin_loader):
    plugin_loader.class_name = 'test_class'
    mock_get_plugin_class.return_value = 'test_type'
    mock_C.CONFIGURABLE_PLUGINS = ['test_type']
    mock_module = MagicMock()
    mock_module.DOCUMENTATION = 'mock_documentation'
    mock_AnsibleLoader.return_value.get_single_data.return_value = {'options': {'key': 'value'}}
    
    plugin_loader._load_config_defs('test_name', mock_module, 'test_path')
    
    mock_get_plugin_class.assert_called_once_with('test_class')
    mock_AnsibleLoader.assert_called_once_with('mock_documentation', file_name='test_path')
    mock_add_fragments.assert_called_once()
    mock_C.config.initialize_plugin_configuration_definitions.assert_called_once_with('test_type', 'test_name', {'key': 'value'})
    mock_display.debug.assert_called_once_with('Loaded config def from plugin (test_type/test_name)')

def test_load_config_defs_with_class_name_not_configurable(plugin_loader):
    with patch('ansible.plugins.loader.get_plugin_class', return_value='non_configurable_type'), \
         patch('ansible.plugins.loader.C.CONFIGURABLE_PLUGINS', new_callable=list):
        plugin_loader.class_name = 'test_class'
        plugin_loader._load_config_defs('test_name', MagicMock(), 'test_path')
        # No assertions needed as we are testing non-execution of code

def test_load_config_defs_with_no_dstring(plugin_loader):
    with patch('ansible.plugins.loader.get_plugin_class', return_value='test_type'), \
         patch('ansible.plugins.loader.C.CONFIGURABLE_PLUGINS', ['test_type']), \
         patch('ansible.plugins.loader.AnsibleLoader') as mock_AnsibleLoader:
        mock_AnsibleLoader.return_value.get_single_data.return_value = None
        plugin_loader.class_name = 'test_class'
        plugin_loader._load_config_defs('test_name', MagicMock(), 'test_path')
        # No assertions needed as we are testing non-execution of code

def test_load_config_defs_with_dstring_no_options(plugin_loader):
    with patch('ansible.plugins.loader.get_plugin_class', return_value='test_type'), \
         patch('ansible.plugins.loader.C.CONFIGURABLE_PLUGINS', ['test_type']), \
         patch('ansible.plugins.loader.AnsibleLoader') as mock_AnsibleLoader:
        mock_AnsibleLoader.return_value.get_single_data.return_value = {}
        plugin_loader.class_name = 'test_class'
        plugin_loader._load_config_defs('test_name', MagicMock(), 'test_path')
        # No assertions needed as we are testing non-execution of code
