# file lib/ansible/plugins/loader.py:761-770
# lines [764, 765, 766, 767, 768, 770]
# branches ['767->768', '767->770']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import PluginLoader
from ansible.utils.display import Display

@pytest.fixture
def plugin_loader(mocker):
    # Mock the __init__ method of PluginLoader to bypass the required arguments
    mocker.patch.object(PluginLoader, '__init__', lambda self: None)
    # Manually set the attributes that would be set by the real __init__ method
    plugin_loader = PluginLoader()
    plugin_loader.class_name = 'test_class'
    plugin_loader.package = 'test_package'
    plugin_loader.config = 'test_config'
    plugin_loader.subdir = 'test_subdir'
    return plugin_loader

def test_has_plugin_exception_handling(plugin_loader, mocker):
    # Mock the find_plugin method to raise a generic exception
    mocker.patch.object(plugin_loader, 'find_plugin', side_effect=Exception('Test Exception'))
    
    # Mock the display.debug method to verify it gets called
    mock_display_debug = mocker.patch.object(Display, 'debug')
    
    # Call the has_plugin method and assert it returns None
    result = plugin_loader.has_plugin('test_plugin')
    assert result is None
    
    # Verify that display.debug was called with the expected message
    mock_display_debug.assert_called_once_with('has_plugin error: Test Exception')

def test_has_plugin_ansible_error(plugin_loader, mocker):
    # Mock the find_plugin method to raise an AnsibleError
    mocker.patch.object(plugin_loader, 'find_plugin', side_effect=AnsibleError('Test AnsibleError'))
    
    # Call the has_plugin method and assert it raises AnsibleError
    with pytest.raises(AnsibleError, match='Test AnsibleError'):
        plugin_loader.has_plugin('test_plugin')
