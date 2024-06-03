# file lib/ansible/config/manager.py:421-431
# lines [421, 424, 425, 426, 427, 428, 429, 430, 431]
# branches []

import pytest
from unittest.mock import Mock, patch
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_get_config_value_handles_ansible_error(config_manager):
    with patch.object(config_manager, 'get_config_value_and_origin', side_effect=AnsibleError("Test AnsibleError")):
        with pytest.raises(AnsibleError, match="Test AnsibleError"):
            config_manager.get_config_value('some_config')

def test_get_config_value_handles_generic_exception(config_manager):
    with patch.object(config_manager, 'get_config_value_and_origin', side_effect=Exception("Test Exception")):
        with pytest.raises(AnsibleError) as excinfo:
            config_manager.get_config_value('some_config')
        assert "Unhandled exception when retrieving some_config" in str(excinfo.value)
        assert "Test Exception" in str(excinfo.value)

def test_get_config_value_success(config_manager):
    with patch.object(config_manager, 'get_config_value_and_origin', return_value=('expected_value', 'origin')):
        result = config_manager.get_config_value('some_config')
        assert result == 'expected_value'
