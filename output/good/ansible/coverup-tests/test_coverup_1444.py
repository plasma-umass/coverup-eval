# file lib/ansible/config/manager.py:421-431
# lines [428]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.config.manager import ConfigManager
from ansible.module_utils._text import to_native

@pytest.fixture
def config_manager(mocker):
    mocker.patch.object(ConfigManager, '__init__', return_value=None)
    config_manager = ConfigManager()
    config_manager._config_file = None
    config_manager._base_defs = {}
    config_manager.data = mocker.MagicMock()
    return config_manager

def test_get_config_value_exception_handling(config_manager, mocker):
    mocker.patch.object(ConfigManager, 'get_config_value_and_origin', side_effect=AnsibleError("Test induced AnsibleError"))
    
    with pytest.raises(AnsibleError):
        config_manager.get_config_value('some_config')

def test_get_config_value_unhandled_exception_handling(config_manager, mocker):
    def raise_unhandled_exception(*args, **kwargs):
        raise ValueError("This is an unhandled exception")

    mocker.patch.object(ConfigManager, 'get_config_value_and_origin', side_effect=raise_unhandled_exception)

    with pytest.raises(AnsibleError) as exc_info:
        config_manager.get_config_value('some_config')

    assert "Unhandled exception when retrieving some_config" in str(exc_info.value)
    assert "This is an unhandled exception" in str(exc_info.value)
