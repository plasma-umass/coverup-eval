# file lib/ansible/plugins/loader.py:1004-1010
# lines [1004, 1006, 1007, 1010]
# branches ['1006->1007', '1006->1010']

import pytest
from ansible.plugins.loader import PluginLoader, Jinja2Loader
from ansible.errors import AnsibleError

class MockPluginLoader(PluginLoader):
    def __init__(self, class_name, package, config, subdir):
        self.class_name = class_name
        self.package = package
        self.config = config
        self.subdir = subdir

def test_jinja2loader_find_plugin_with_dot(mocker):
    mocker.patch.object(PluginLoader, 'find_plugin', return_value='mocked_plugin')
    mocker.patch('ansible.plugins.loader.PluginLoader', MockPluginLoader)
    loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
    result = loader.find_plugin('plugin.with.dot')
    assert result == 'mocked_plugin'

def test_jinja2loader_find_plugin_without_dot(mocker):
    mocker.patch('ansible.plugins.loader.PluginLoader', MockPluginLoader)
    loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
    with pytest.raises(AnsibleError, match='No code should call "find_plugin" for Jinja2Loaders \(Not implemented\)'):
        loader.find_plugin('plugin_without_dot')
