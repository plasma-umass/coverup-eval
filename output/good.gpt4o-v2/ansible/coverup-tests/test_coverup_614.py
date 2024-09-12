# file: lib/ansible/plugins/loader.py:1004-1010
# asked: {"lines": [1004, 1006, 1007, 1010], "branches": [[1006, 1007], [1006, 1010]]}
# gained: {"lines": [1004, 1006, 1010], "branches": [[1006, 1010]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader, PluginLoader

class MockPluginLoader(PluginLoader):
    def find_plugin(self, name, collection_list=None):
        return f"Plugin: {name}, Collections: {collection_list}"

@pytest.fixture
def jinja2_loader():
    return Jinja2Loader(class_name='jinja2', package='ansible.plugins', config=None, subdir='jinja2')

def test_find_plugin_with_dot_in_name(monkeypatch, jinja2_loader):
    def mock_super_find_plugin(self, name, collection_list=None):
        return f"Mocked Plugin: {name}, Collections: {collection_list}"
    
    monkeypatch.setattr(MockPluginLoader, 'find_plugin', mock_super_find_plugin)
    jinja2_loader.__class__ = MockPluginLoader
    
    result = jinja2_loader.find_plugin('plugin.name')
    assert result == "Mocked Plugin: plugin.name, Collections: None"

def test_find_plugin_without_dot_in_name(jinja2_loader):
    with pytest.raises(AnsibleError, match='No code should call "find_plugin" for Jinja2Loaders \(Not implemented\)'):
        jinja2_loader.find_plugin('pluginname')
