# file: lib/ansible/plugins/loader.py:1012-1018
# asked: {"lines": [1012, 1014, 1015, 1018], "branches": [[1014, 1015], [1014, 1018]]}
# gained: {"lines": [1012, 1014, 1018], "branches": [[1014, 1018]]}

import pytest
from ansible.plugins.loader import PluginLoader, Jinja2Loader
from ansible.errors import AnsibleError

class MockPluginLoader(PluginLoader):
    def __init__(self):
        pass

    def get(self, name, *args, **kwargs):
        return f"MockPlugin: {name}"

@pytest.fixture
def mock_plugin_loader(monkeypatch):
    monkeypatch.setattr(Jinja2Loader, 'get', MockPluginLoader().get)

def test_jinja2loader_get_with_dot(mock_plugin_loader):
    loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
    result = loader.get('plugin.name')
    assert result == "MockPlugin: plugin.name"

def test_jinja2loader_get_without_dot():
    loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
    with pytest.raises(AnsibleError, match='No code should call "get" for Jinja2Loaders \(Not implemented\)'):
        loader.get('pluginname')
