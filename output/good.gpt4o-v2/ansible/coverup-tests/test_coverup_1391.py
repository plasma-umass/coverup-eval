# file: lib/ansible/plugins/loader.py:1012-1018
# asked: {"lines": [1014, 1015, 1018], "branches": [[1014, 1015], [1014, 1018]]}
# gained: {"lines": [1014, 1015, 1018], "branches": [[1014, 1015], [1014, 1018]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader, PluginLoader

class MockPluginLoader(PluginLoader):
    def get(self, name, *args, **kwargs):
        return f"Mocked get with {name}"

@pytest.fixture
def jinja2_loader():
    return Jinja2Loader(class_name='test_class', package='test_package', config=None, subdir='test_subdir')

def test_jinja2_loader_get_with_dot(monkeypatch, jinja2_loader):
    original_bases = Jinja2Loader.__bases__
    Jinja2Loader.__bases__ = (MockPluginLoader,)
    
    def mock_super_get(self, name, *args, **kwargs):
        return f"Mocked get with {name}"

    monkeypatch.setattr(MockPluginLoader, 'get', mock_super_get)

    try:
        result = jinja2_loader.get('test.plugin')
        assert result == "Mocked get with test.plugin"
    finally:
        Jinja2Loader.__bases__ = original_bases

def test_jinja2_loader_get_without_dot(jinja2_loader):
    with pytest.raises(AnsibleError, match='No code should call "get" for Jinja2Loaders \(Not implemented\)'):
        jinja2_loader.get('testplugin')
