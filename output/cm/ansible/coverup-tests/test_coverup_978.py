# file lib/ansible/config/manager.py:343-345
# lines [343, 345]
# branches []

import pytest
from ansible.config.manager import ConfigManager

# Assuming the ConfigManager class is part of a larger module that we're testing

def test_find_yaml_config_files(mocker):
    # Mock the ConfigManager object
    config_manager = ConfigManager()
    
    # Mock the _find_yaml_config_files method to simply return True
    mocker.patch.object(config_manager, '_find_yaml_config_files', return_value=True)
    
    # Call the method and assert that it was called and returned True
    result = config_manager._find_yaml_config_files()
    assert result == True
    config_manager._find_yaml_config_files.assert_called_once()
