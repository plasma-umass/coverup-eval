# file: lib/ansible/plugins/loader.py:1012-1018
# asked: {"lines": [1012, 1014, 1015, 1018], "branches": [[1014, 1015], [1014, 1018]]}
# gained: {"lines": [1012, 1014, 1018], "branches": [[1014, 1018]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader, PluginLoader

class MockPluginLoader(PluginLoader):
    def __init__(self):
        pass

    def get(self, name, *args, **kwargs):
        return f"Mock plugin {name}"

class MockJinja2Loader(Jinja2Loader):
    def __init__(self):
        super().__init__('class_name', 'package', 'config', 'subdir')

def test_jinja2loader_get_with_dot(monkeypatch):
    loader = MockJinja2Loader()
    monkeypatch.setattr(loader, 'get', MockPluginLoader().get)
    result = loader.get('plugin.with.dot')
    assert result == "Mock plugin plugin.with.dot"

def test_jinja2loader_get_without_dot():
    loader = MockJinja2Loader()
    with pytest.raises(AnsibleError, match='No code should call "get" for Jinja2Loaders \(Not implemented\)'):
        loader.get('plugin_without_dot')
