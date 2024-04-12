# file thefuck/conf.py:91-107
# lines [107]
# branches ['104->107']

import os
import pytest
from thefuck.conf import Settings

@pytest.fixture
def settings():
    return Settings()

@pytest.fixture
def env_var(monkeypatch):
    monkeypatch.setenv('THEFUCK_TEST_ENV_VAR', 'test_value')
    yield
    monkeypatch.delenv('THEFUCK_TEST_ENV_VAR', raising=False)

def test_val_from_env_with_unhandled_attr(settings, env_var):
    assert settings._val_from_env('THEFUCK_TEST_ENV_VAR', 'unhandled_attr') == 'test_value'
