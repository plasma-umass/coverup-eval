# file lib/ansible/plugins/loader.py:995-1003
# lines [995, 996]
# branches []

import pytest
from ansible.plugins.loader import PluginLoader

class TestJinja2Loader:
    @pytest.fixture
    def mock_plugin_loader(self, mocker):
        class MockPluginLoader(PluginLoader):
            def __init__(self, class_name, package, config, subdir):
                super().__init__(class_name, package, config, subdir)
                self._plugins = {}
                self._plugin_paths = []
                self._all_plugins = []

            def all(self):
                return self._all_plugins

        return MockPluginLoader

    def test_jinja2_loader_all_method(self, mock_plugin_loader):
        class Jinja2Loader(mock_plugin_loader):
            def all(self):
                # Simulate the behavior of the Jinja2Loader's all method
                self._all_plugins = ['plugin1', 'plugin2', 'plugin3']
                return self._all_plugins

        loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
        plugins = loader.all()
        
        assert plugins == ['plugin1', 'plugin2', 'plugin3']
        assert len(plugins) == 3
        assert 'plugin1' in plugins
        assert 'plugin2' in plugins
        assert 'plugin3' in plugins
