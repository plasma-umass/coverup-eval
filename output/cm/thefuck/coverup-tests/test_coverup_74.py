# file thefuck/conf.py:11-12
# lines [11, 12]
# branches []

import pytest
from thefuck.conf import Settings

def test_settings_getattr():
    settings = Settings({'attribute': 'value'})
    
    # Test that the __getattr__ method returns the correct value
    assert settings.attribute == 'value'
    
    # Test that the __getattr__ method returns None for a missing attribute
    assert settings.missing_attribute is None
