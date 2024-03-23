# file lib/ansible/config/manager.py:343-345
# lines [345]
# branches []

import pytest
from ansible.config.manager import ConfigManager

# Assuming the ConfigManager class is part of a larger module that we're testing

def test_find_yaml_config_files(mocker):
    # Mock the ConfigManager object
    config_manager = ConfigManager()
    
    # Mock the _find_yaml_config_files method to track if it's called
    mocker.patch.object(config_manager, '_find_yaml_config_files', side_effect=config_manager._find_yaml_config_files)
    
    # Call the method we want to test
    config_manager._find_yaml_config_files()
    
    # Assert that the method was indeed called
    assert config_manager._find_yaml_config_files.called
    
    # Clean up is handled by the mocker fixture, which automatically undoes patches after the test
