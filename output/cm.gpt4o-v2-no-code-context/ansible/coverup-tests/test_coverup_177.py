# file: lib/ansible/plugins/lookup/config.py:88-104
# asked: {"lines": [88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104], "branches": [[93, 94], [93, 95], [100, 101], [100, 102]]}
# gained: {"lines": [88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104], "branches": [[93, 94], [93, 95], [100, 101], [100, 102]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleLookupError, AnsibleError
from ansible.plugins.lookup.config import _get_plugin_config, MissingSetting

@pytest.fixture
def mock_plugin_loader(monkeypatch):
    mock_loader = MagicMock()
    monkeypatch.setattr('ansible.plugins.lookup.config.plugin_loader', mock_loader)
    return mock_loader

@pytest.fixture
def mock_config(monkeypatch):
    mock_config = MagicMock()
    monkeypatch.setattr('ansible.plugins.lookup.config.C.config', mock_config)
    return mock_config

def test_get_plugin_config_success(mock_plugin_loader, mock_config):
    mock_plugin = MagicMock()
    mock_plugin_loader.lookup_loader.get.return_value = mock_plugin
    mock_plugin._load_name = 'test_plugin'
    mock_config.get_config_value.return_value = 'test_value'

    result = _get_plugin_config('test_plugin', 'lookup', 'test_config', 'test_variables')
    
    assert result == 'test_value'
    mock_plugin_loader.lookup_loader.get.assert_called_once_with('test_plugin', class_only=True)
    mock_config.get_config_value.assert_called_once_with('test_config', plugin_type='lookup', plugin_name='test_plugin', variables='test_variables')

def test_get_plugin_config_plugin_not_found(mock_plugin_loader):
    mock_plugin_loader.lookup_loader.get.return_value = None

    with pytest.raises(AnsibleLookupError, match='Unable to load lookup plugin "test_plugin"'):
        _get_plugin_config('test_plugin', 'lookup', 'test_config', 'test_variables')

def test_get_plugin_config_ansible_error(mock_plugin_loader):
    mock_plugin = MagicMock()
    mock_plugin_loader.lookup_loader.get.return_value = mock_plugin
    mock_plugin._load_name = 'test_plugin'
    
    with patch('ansible.plugins.lookup.config.C.config.get_config_value', side_effect=AnsibleError('was not defined')):
        with pytest.raises(MissingSetting, match='was not defined'):
            _get_plugin_config('test_plugin', 'lookup', 'test_config', 'test_variables')

    with patch('ansible.plugins.lookup.config.C.config.get_config_value', side_effect=AnsibleError('some other error')):
        with pytest.raises(AnsibleError, match='some other error'):
            _get_plugin_config('test_plugin', 'lookup', 'test_config', 'test_variables')
