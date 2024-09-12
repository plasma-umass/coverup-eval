# file: lib/ansible/config/manager.py:421-431
# asked: {"lines": [421, 424, 425, 426, 427, 428, 429, 430, 431], "branches": []}
# gained: {"lines": [421, 424, 425, 426, 427, 428, 429, 430, 431], "branches": []}

import pytest
from ansible.errors import AnsibleError
from ansible.config.manager import ConfigManager

class MockConfigManager(ConfigManager):
    def get_config_value_and_origin(self, config, cfile=None, plugin_type=None, plugin_name=None, keys=None, variables=None, direct=None):
        if config == "raise_ansible_error":
            raise AnsibleError("Ansible error")
        elif config == "raise_exception":
            raise Exception("General exception")
        return "mock_value", "mock_origin"

@pytest.fixture
def config_manager():
    return MockConfigManager()

def test_get_config_value_success(config_manager):
    result = config_manager.get_config_value("valid_config")
    assert result == "mock_value"

def test_get_config_value_ansible_error(config_manager):
    with pytest.raises(AnsibleError, match="Ansible error"):
        config_manager.get_config_value("raise_ansible_error")

def test_get_config_value_general_exception(config_manager):
    with pytest.raises(AnsibleError, match="Unhandled exception when retrieving raise_exception"):
        config_manager.get_config_value("raise_exception")
