# file lib/ansible/config/manager.py:277-281
# lines [277, 279, 280]
# branches []

import pytest
from ansible.config.manager import ConfigManager

# Since the actual methods to add deprecations and warnings do not exist,
# we will directly manipulate the class variables for the purpose of this test.

def test_config_manager_deprecated_and_warnings():
    # Setup
    config_manager = ConfigManager()
    
    # Test that DEPRECATED and WARNINGS are initially empty
    assert config_manager.DEPRECATED == []
    assert config_manager.WARNINGS == set()
    
    # Simulate deprecation and warning scenarios by directly adding to the class variables
    ConfigManager.DEPRECATED.append('deprecated_feature')
    ConfigManager.WARNINGS.add('warning_message')
    
    # Test that DEPRECATED and WARNINGS are no longer empty
    assert 'deprecated_feature' in ConfigManager.DEPRECATED
    assert 'warning_message' in ConfigManager.WARNINGS
    
    # Cleanup by removing the added deprecation and warning
    ConfigManager.DEPRECATED.remove('deprecated_feature')
    ConfigManager.WARNINGS.remove('warning_message')
    
    # Test that DEPRECATED and WARNINGS are empty again
    assert config_manager.DEPRECATED == []
    assert config_manager.WARNINGS == set()
