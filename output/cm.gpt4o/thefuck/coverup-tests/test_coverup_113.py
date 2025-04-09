# file thefuck/conf.py:109-113
# lines [111, 112, 113]
# branches []

import os
import pytest
from unittest import mock
from thefuck.conf import Settings
import thefuck.const as const

@pytest.fixture
def mock_env_vars():
    original_env = os.environ.copy()
    os.environ['TEST_ENV_VAR'] = 'test_value'
    const.ENV_TO_ATTR = {'TEST_ENV_VAR': 'test_attr'}
    yield
    os.environ.clear()
    os.environ.update(original_env)

def test_settings_from_env(mock_env_vars):
    settings = Settings()
    result = settings._settings_from_env()
    assert result == {'test_attr': 'test_value'}
