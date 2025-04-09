# file lib/ansible/config/manager.py:343-345
# lines [345]
# branches []

import pytest
from ansible.config.manager import ConfigManager

def test_find_yaml_config_files_executes():
    config_manager = ConfigManager()

    # Call the method
    result = config_manager._find_yaml_config_files()

    # Assertions to verify the method was called and returned None
    assert result is None
