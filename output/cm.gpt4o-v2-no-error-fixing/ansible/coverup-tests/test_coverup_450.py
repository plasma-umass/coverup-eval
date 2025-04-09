# file: lib/ansible/plugins/loader.py:799-804
# asked: {"lines": [799, 802, 803, 804], "branches": []}
# gained: {"lines": [799, 802, 803, 804], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='test_class', package='test_package', config=None, subdir='test_subdir')

def test_update_object(plugin_loader):
    mock_obj = Mock()
    name = 'test_name'
    path = 'test_path'
    redirected_names = ['name1', 'name2']

    plugin_loader._update_object(mock_obj, name, path, redirected_names)

    assert mock_obj._original_path == path
    assert mock_obj._load_name == name
    assert mock_obj._redirected_names == redirected_names

def test_update_object_no_redirected_names(plugin_loader):
    mock_obj = Mock()
    name = 'test_name'
    path = 'test_path'

    plugin_loader._update_object(mock_obj, name, path)

    assert mock_obj._original_path == path
    assert mock_obj._load_name == name
    assert mock_obj._redirected_names == []
