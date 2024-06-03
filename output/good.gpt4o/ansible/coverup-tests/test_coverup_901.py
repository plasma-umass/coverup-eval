# file lib/ansible/config/manager.py:343-345
# lines [343, 345]
# branches []

import pytest
from unittest.mock import patch
from ansible.config.manager import ConfigManager

@pytest.fixture
def config_manager():
    return ConfigManager()

def test_find_yaml_config_files(config_manager):
    with patch.object(ConfigManager, '_find_yaml_config_files', return_value=None) as mock_method:
        result = config_manager._find_yaml_config_files()
        mock_method.assert_called_once()
        assert result is None
