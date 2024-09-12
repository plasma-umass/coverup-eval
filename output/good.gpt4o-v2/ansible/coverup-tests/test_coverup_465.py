# file: lib/ansible/config/manager.py:421-431
# asked: {"lines": [421, 424, 425, 426, 427, 428, 429, 430, 431], "branches": []}
# gained: {"lines": [421, 424, 425, 426, 427, 428, 429, 430, 431], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.config.manager import ConfigManager

def test_get_config_value_success(mocker):
    config_manager = ConfigManager()
    mock_get_config_value_and_origin = mocker.patch.object(
        config_manager, 'get_config_value_and_origin', return_value=('value', 'origin')
    )
    
    result = config_manager.get_config_value('some_config')
    
    mock_get_config_value_and_origin.assert_called_once_with(
        'some_config', cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None
    )
    assert result == 'value'

def test_get_config_value_ansible_error(mocker):
    config_manager = ConfigManager()
    mock_get_config_value_and_origin = mocker.patch.object(
        config_manager, 'get_config_value_and_origin', side_effect=AnsibleError('Ansible error')
    )
    
    with pytest.raises(AnsibleError, match='Ansible error'):
        config_manager.get_config_value('some_config')
    
    mock_get_config_value_and_origin.assert_called_once_with(
        'some_config', cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None
    )

def test_get_config_value_unhandled_exception(mocker):
    config_manager = ConfigManager()
    mock_get_config_value_and_origin = mocker.patch.object(
        config_manager, 'get_config_value_and_origin', side_effect=Exception('Unhandled exception')
    )
    
    with pytest.raises(AnsibleError, match='Unhandled exception when retrieving some_config'):
        config_manager.get_config_value('some_config')
    
    mock_get_config_value_and_origin.assert_called_once_with(
        'some_config', cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None
    )
