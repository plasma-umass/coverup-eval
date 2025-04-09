# file: lib/ansible/config/manager.py:421-431
# asked: {"lines": [421, 424, 425, 426, 427, 428, 429, 430, 431], "branches": []}
# gained: {"lines": [421, 424, 425, 426, 427, 428, 429, 430, 431], "branches": []}

import pytest
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError
from unittest.mock import patch

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_config_value_success(config_manager, mocker):
    mocker.patch.object(config_manager, 'get_config_value_and_origin', return_value=('value', None))
    result = config_manager.get_config_value('some_config')
    assert result == 'value'

def test_get_config_value_ansible_error(config_manager, mocker):
    mocker.patch.object(config_manager, 'get_config_value_and_origin', side_effect=AnsibleError)
    with pytest.raises(AnsibleError):
        config_manager.get_config_value('some_config')

def test_get_config_value_unhandled_exception(config_manager, mocker):
    mocker.patch.object(config_manager, 'get_config_value_and_origin', side_effect=Exception('unexpected error'))
    with pytest.raises(AnsibleError) as excinfo:
        config_manager.get_config_value('some_config')
    assert 'Unhandled exception when retrieving some_config' in str(excinfo.value)
    assert 'unexpected error' in str(excinfo.value)
