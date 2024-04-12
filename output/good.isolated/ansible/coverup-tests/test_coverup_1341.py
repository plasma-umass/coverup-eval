# file lib/ansible/plugins/loader.py:1004-1010
# lines [1006, 1007, 1010]
# branches ['1006->1007', '1006->1010']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import Jinja2Loader

@pytest.fixture
def jinja2_loader(mocker):
    mocker.patch('ansible.plugins.loader.PluginLoader.__init__', return_value=None)
    return Jinja2Loader('dummy_class', 'dummy_package', 'dummy_config', 'dummy_subdir')

def test_jinja2_loader_find_plugin_with_dot(jinja2_loader, mocker):
    mocker.patch.object(Jinja2Loader, 'find_plugin', return_value='path/to/plugin')
    
    # Test with a plugin name containing a dot
    plugin_name = 'my.plugin'
    collection_list = ['my_collection']
    result = jinja2_loader.find_plugin(plugin_name, collection_list=collection_list)

    assert result == 'path/to/plugin'
    Jinja2Loader.find_plugin.assert_called_once_with(plugin_name, collection_list=collection_list)

def test_jinja2_loader_find_plugin_without_dot(jinja2_loader):
    # Test with a plugin name without a dot, expecting an exception
    plugin_name = 'my_plugin'
    with pytest.raises(AnsibleError) as excinfo:
        jinja2_loader.find_plugin(plugin_name)

    assert str(excinfo.value) == 'No code should call "find_plugin" for Jinja2Loaders (Not implemented)'
