# file lib/ansible/config/manager.py:421-431
# lines [421, 424, 425, 426, 427, 428, 429, 430, 431]
# branches []

import pytest
from ansible.errors import AnsibleError
from ansible.config.manager import ConfigManager
from ansible.module_utils._text import to_native

@pytest.fixture
def config_manager(mocker):
    mocker.patch.object(ConfigManager, '__init__', return_value=None)
    mocker.patch.object(ConfigManager, 'update_config_data', return_value=None)
    cm = ConfigManager()
    cm._config_file = None
    cm._base_defs = {}
    cm.data = mocker.MagicMock()
    return cm

def test_get_config_value_exception_handling(config_manager, mocker):
    mocker.patch.object(ConfigManager, 'get_config_value_and_origin', side_effect=Exception("Test Exception"))
    
    with pytest.raises(AnsibleError) as excinfo:
        config_manager.get_config_value('test_config')

    assert "Unhandled exception when retrieving test_config" in str(excinfo.value)
    assert "Test Exception" in str(excinfo.value)
