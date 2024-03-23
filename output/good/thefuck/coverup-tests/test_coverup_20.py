# file thefuck/conf.py:75-80
# lines [75, 77, 78, 79, 80]
# branches ['78->79', '78->80']

import os
import pytest
from thefuck import conf, const

# Assuming the Settings class is in thefuck.conf module and const.DEFAULT_RULES is defined

@pytest.fixture
def settings():
    return conf.Settings()

@pytest.fixture
def environment_cleanup():
    # Fixture to clean up environment variables after each test
    original_env = os.environ.copy()
    yield
    os.environ = original_env

def test_rules_from_env_with_default_rules(settings, environment_cleanup):
    # Set up the environment variable with 'DEFAULT_RULES'
    os.environ['THEFUCK_RULES'] = 'DEFAULT_RULES:some_rule:another_rule'
    # Mock the DEFAULT_RULES
    const.DEFAULT_RULES = ['default_rule1', 'default_rule2']
    # Call the method to test
    rules = settings._rules_from_env(os.environ['THEFUCK_RULES'])
    # Check if the DEFAULT_RULES are included and the 'DEFAULT_RULES' placeholder is removed
    assert rules == ['default_rule1', 'default_rule2', 'some_rule', 'another_rule']
