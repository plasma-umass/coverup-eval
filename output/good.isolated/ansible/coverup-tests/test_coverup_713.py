# file lib/ansible/plugins/loader.py:799-804
# lines [799, 802, 803, 804]
# branches []

import pytest
from ansible.plugins.loader import PluginLoader
from unittest.mock import MagicMock

class MockPluginLoader(PluginLoader):
    def __init__(self):
        pass  # Bypass the original constructor

class TestPluginLoader:
    @pytest.fixture
    def plugin_loader(self):
        return MockPluginLoader()

    def test_update_object(self, plugin_loader):
        obj = type('TestPlugin', (object,), {})()
        name = 'test_plugin'
        path = '/path/to/plugin'
        redirected_names = ['redirected_plugin']

        plugin_loader._update_object(obj, name, path, redirected_names)

        assert hasattr(obj, '_original_path')
        assert obj._original_path == path
        assert hasattr(obj, '_load_name')
        assert obj._load_name == name
        assert hasattr(obj, '_redirected_names')
        assert obj._redirected_names == redirected_names

        # Test with default redirected_names
        plugin_loader._update_object(obj, name, path)
        assert obj._redirected_names == []
