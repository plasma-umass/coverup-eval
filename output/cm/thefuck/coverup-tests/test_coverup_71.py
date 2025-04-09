# file thefuck/conf.py:14-15
# lines [14, 15]
# branches []

import pytest
from thefuck.conf import Settings

def test_settings_setattr():
    settings = Settings()
    settings.__setattr__('test_key', 'test_value')
    assert settings['test_key'] == 'test_value'
