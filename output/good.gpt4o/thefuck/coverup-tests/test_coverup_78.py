# file thefuck/conf.py:14-15
# lines [14, 15]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Settings class is imported from thefuck.conf
from thefuck.conf import Settings

def test_settings_setattr():
    settings = Settings()
    
    # Test setting an attribute
    settings.some_key = 'some_value'
    assert settings['some_key'] == 'some_value'
    
    # Test updating an attribute
    settings.some_key = 'new_value'
    assert settings['some_key'] == 'new_value'
    
    # Test setting another attribute
    settings.another_key = 123
    assert settings['another_key'] == 123

    # Clean up
    del settings['some_key']
    del settings['another_key']
    assert 'some_key' not in settings
    assert 'another_key' not in settings
