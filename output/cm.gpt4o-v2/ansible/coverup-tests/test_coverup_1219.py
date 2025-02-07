# file: lib/ansible/plugins/loader.py:761-770
# asked: {"lines": [766, 767, 768, 770], "branches": [[767, 768], [767, 770]]}
# gained: {"lines": [766, 767, 768, 770], "branches": [[767, 768], [767, 770]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='test_class', package='test_package', config=None, subdir='plugins')

def test_has_plugin_with_ansible_error(plugin_loader):
    with patch.object(plugin_loader, 'find_plugin', side_effect=AnsibleError("Test AnsibleError")):
        with pytest.raises(AnsibleError):
            plugin_loader.has_plugin("test_plugin")

def test_has_plugin_with_generic_exception(plugin_loader, mocker):
    mock_display = mocker.patch('ansible.plugins.loader.display')
    with patch.object(plugin_loader, 'find_plugin', side_effect=Exception("Test Exception")):
        result = plugin_loader.has_plugin("test_plugin")
        assert result is None
        mock_display.debug.assert_called_once_with('has_plugin error: Test Exception')
