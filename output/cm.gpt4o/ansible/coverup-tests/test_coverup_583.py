# file lib/ansible/plugins/loader.py:1012-1018
# lines [1012, 1014, 1015, 1018]
# branches ['1014->1015', '1014->1018']

import pytest
from ansible.plugins.loader import PluginLoader, Jinja2Loader
from ansible.errors import AnsibleError

class MockPluginLoader(PluginLoader):
    def __init__(self, *args, **kwargs):
        pass

    def get(self, name, *args, **kwargs):
        return f"Mock plugin {name}"

@pytest.fixture
def mock_plugin_loader(mocker):
    mocker.patch('ansible.plugins.loader.PluginLoader.get', MockPluginLoader().get)

def test_jinja2loader_get_with_dot(mock_plugin_loader):
    loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
    result = loader.get('plugin.with.dot')
    assert result == "Mock plugin plugin.with.dot"

def test_jinja2loader_get_without_dot():
    loader = Jinja2Loader('class_name', 'package', 'config', 'subdir')
    with pytest.raises(AnsibleError, match='No code should call "get" for Jinja2Loaders \(Not implemented\)'):
        loader.get('plugin_without_dot')
