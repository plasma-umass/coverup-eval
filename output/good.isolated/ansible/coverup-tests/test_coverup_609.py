# file lib/ansible/plugins/loader.py:1012-1018
# lines [1012, 1014, 1015, 1018]
# branches ['1014->1015', '1014->1018']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader

# Assuming the Jinja2Loader is part of a larger module that we're testing

@pytest.fixture
def jinja2_loader(mocker):
    mocker.patch('ansible.plugins.loader.PluginLoader.__init__', return_value=None)
    return Jinja2Loader('dummy_class', 'dummy_package', 'dummy_config', 'dummy_subdir')

def test_jinja2_loader_get_with_dot(mocker, jinja2_loader):
    mocker.patch('ansible.plugins.loader.PluginLoader.get', return_value='mocked_plugin')
    plugin_name = 'my.plugin'
    result = jinja2_loader.get(plugin_name)
    assert result == 'mocked_plugin'

def test_jinja2_loader_get_without_dot(jinja2_loader):
    with pytest.raises(AnsibleError) as excinfo:
        jinja2_loader.get('my_plugin')
    assert 'No code should call "get" for Jinja2Loaders' in str(excinfo.value)
