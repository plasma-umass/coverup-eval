# file thefuck/conf.py:82-89
# lines [82, 84, 85, 86, 87, 88, 89]
# branches ['84->exit', '84->85']

import pytest
from unittest.mock import patch

# Assuming the Settings class is imported from thefuck.conf
from thefuck.conf import Settings

@pytest.fixture
def settings():
    return Settings()

def test_priority_from_env(settings):
    env_value = "rule1=10:rule2=20:invalid_rule:rule3=30"
    expected_output = [("rule1", 10), ("rule2", 20), ("rule3", 30)]
    
    result = list(settings._priority_from_env(env_value))
    
    assert result == expected_output

def test_priority_from_env_invalid(settings):
    env_value = "invalid_rule"
    expected_output = []
    
    result = list(settings._priority_from_env(env_value))
    
    assert result == expected_output
