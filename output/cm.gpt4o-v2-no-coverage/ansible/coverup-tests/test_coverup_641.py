# file: lib/ansible/plugins/loader.py:1004-1010
# asked: {"lines": [1004, 1006, 1007, 1010], "branches": [[1006, 1007], [1006, 1010]]}
# gained: {"lines": [1004, 1006, 1010], "branches": [[1006, 1010]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader, PluginLoader

class MockPluginLoader(PluginLoader):
    def __init__(self):
        pass

    def find_plugin(self, name, collection_list=None):
        return f"Plugin: {name}, Collections: {collection_list}"

def test_find_plugin_with_dot(monkeypatch):
    loader = Jinja2Loader(class_name='test', package='test', config=None, subdir='test')
    monkeypatch.setattr(loader, 'find_plugin', MockPluginLoader().find_plugin)
    
    result = loader.find_plugin('plugin.with.dot')
    assert result == "Plugin: plugin.with.dot, Collections: None"

def test_find_plugin_without_dot():
    loader = Jinja2Loader(class_name='test', package='test', config=None, subdir='test')
    
    with pytest.raises(AnsibleError) as excinfo:
        loader.find_plugin('plugin_without_dot')
    
    assert str(excinfo.value) == 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)'
