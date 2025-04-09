# file: lib/ansible/plugins/loader.py:1004-1010
# asked: {"lines": [1004, 1006, 1007, 1010], "branches": [[1006, 1007], [1006, 1010]]}
# gained: {"lines": [1004], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import PluginLoader

class Jinja2Loader(PluginLoader):
    def __init__(self, class_name, package, config, subdir):
        super(Jinja2Loader, self).__init__(class_name, package, config, subdir)

    def find_plugin(self, name, collection_list=None):
        if '.' in name:
            return super(Jinja2Loader, self).find_plugin(name, collection_list=collection_list)
        raise AnsibleError('No code should call "find_plugin" for Jinja2Loaders (Not implemented)')

@pytest.fixture
def jinja2_loader():
    return Jinja2Loader('class_name', 'package', 'config', 'subdir')

def test_find_plugin_with_dot_in_name(monkeypatch, jinja2_loader):
    class MockSuperLoader:
        def find_plugin(self, name, collection_list=None):
            return "mock_plugin"

    monkeypatch.setattr(PluginLoader, 'find_plugin', MockSuperLoader().find_plugin)
    result = jinja2_loader.find_plugin('plugin.name')
    assert result == "mock_plugin"

def test_find_plugin_without_dot_in_name(jinja2_loader):
    with pytest.raises(AnsibleError, match='No code should call "find_plugin" for Jinja2Loaders \(Not implemented\)'):
        jinja2_loader.find_plugin('pluginname')
