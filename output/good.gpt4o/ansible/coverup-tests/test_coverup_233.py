# file lib/ansible/plugins/lookup/config.py:88-104
# lines [88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 104]
# branches ['93->94', '93->95', '100->101', '100->102']

import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.lookup.config import _get_plugin_config, MissingSetting
from ansible.errors import AnsibleLookupError, AnsibleError
from ansible import constants as C
from ansible.module_utils._text import to_native

def test_get_plugin_config_success(mocker):
    pname = 'test_plugin'
    ptype = 'lookup'
    config = 'test_config'
    variables = {}

    mock_loader = mocker.patch('ansible.plugins.lookup.config.plugin_loader.lookup_loader.get', return_value=MagicMock(_load_name='test_plugin'))
    mock_get_config_value = mocker.patch('ansible.plugins.lookup.config.C.config.get_config_value', return_value='test_value')

    result = _get_plugin_config(pname, ptype, config, variables)

    mock_loader.assert_called_once_with(pname, class_only=True)
    mock_get_config_value.assert_called_once_with(config, plugin_type=ptype, plugin_name='test_plugin', variables=variables)
    assert result == 'test_value'

def test_get_plugin_config_plugin_not_found(mocker):
    pname = 'test_plugin'
    ptype = 'lookup'
    config = 'test_config'
    variables = {}

    mock_loader = mocker.patch('ansible.plugins.lookup.config.plugin_loader.lookup_loader.get', return_value=None)

    with pytest.raises(AnsibleLookupError, match='Unable to load lookup plugin "test_plugin"'):
        _get_plugin_config(pname, ptype, config, variables)

    mock_loader.assert_called_once_with(pname, class_only=True)

def test_get_plugin_config_ansible_error(mocker):
    pname = 'test_plugin'
    ptype = 'lookup'
    config = 'test_config'
    variables = {}

    mock_loader = mocker.patch('ansible.plugins.lookup.config.plugin_loader.lookup_loader.get', return_value=MagicMock(_load_name='test_plugin'))
    mock_get_config_value = mocker.patch('ansible.plugins.lookup.config.C.config.get_config_value', side_effect=AnsibleError('test error'))

    with pytest.raises(AnsibleError, match='test error'):
        _get_plugin_config(pname, ptype, config, variables)

    mock_loader.assert_called_once_with(pname, class_only=True)
    mock_get_config_value.assert_called_once_with(config, plugin_type=ptype, plugin_name='test_plugin', variables=variables)

def test_get_plugin_config_missing_setting(mocker):
    pname = 'test_plugin'
    ptype = 'lookup'
    config = 'test_config'
    variables = {}

    mock_loader = mocker.patch('ansible.plugins.lookup.config.plugin_loader.lookup_loader.get', return_value=MagicMock(_load_name='test_plugin'))
    mock_get_config_value = mocker.patch('ansible.plugins.lookup.config.C.config.get_config_value', side_effect=AnsibleError('was not defined'))

    with pytest.raises(MissingSetting, match='was not defined'):
        _get_plugin_config(pname, ptype, config, variables)

    mock_loader.assert_called_once_with(pname, class_only=True)
    mock_get_config_value.assert_called_once_with(config, plugin_type=ptype, plugin_name='test_plugin', variables=variables)
