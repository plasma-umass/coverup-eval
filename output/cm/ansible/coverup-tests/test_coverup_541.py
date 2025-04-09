# file lib/ansible/plugins/loader.py:546-552
# lines [546, 548, 549, 550, 552]
# branches ['549->550', '549->552']

import pytest
from ansible.plugins.loader import PluginLoader
from unittest.mock import MagicMock

@pytest.fixture
def plugin_loader(mocker):
    # Mock the required arguments for PluginLoader
    class_name = 'TestPlugin'
    package = 'test_package'
    config = {}
    subdir = 'test_subdir'

    # Create a PluginLoader instance with mocked arguments
    loader = PluginLoader(class_name, package, config, subdir)

    # Mock the find_plugin_with_context method
    mocker.patch.object(loader, 'find_plugin_with_context')
    return loader

def test_find_plugin_returns_none_when_not_resolved(plugin_loader):
    plugin_loader.find_plugin_with_context.return_value = MagicMock(resolved=False, plugin_resolved_path=None)
    assert plugin_loader.find_plugin('test_plugin') is None

def test_find_plugin_returns_path_when_resolved(plugin_loader):
    expected_path = '/path/to/plugin'
    plugin_loader.find_plugin_with_context.return_value = MagicMock(resolved=True, plugin_resolved_path=expected_path)
    assert plugin_loader.find_plugin('test_plugin') == expected_path
