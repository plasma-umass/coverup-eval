# file: httpie/context.py:88-97
# asked: {"lines": [88, 89, 90, 91, 92, 93, 94, 95, 96], "branches": []}
# gained: {"lines": [88, 89, 90, 91, 92, 93, 94, 95, 96], "branches": []}

import pytest
from httpie.context import Environment
from httpie.config import Config

def test_environment_str_method(monkeypatch):
    # Mock the config property to return a dummy config
    dummy_config = Config()
    monkeypatch.setattr(Environment, 'config', dummy_config)

    # Create an instance of Environment with some valid custom attributes
    env = Environment(stdin_encoding='utf-8', stdout_encoding='utf-8')

    # Add a custom attribute directly to the instance
    env.custom_attr = 'custom_value'

    # Call the __str__ method and verify the output
    env_str = str(env)
    assert 'custom_attr' in env_str
    assert 'custom_value' in env_str
    assert 'config' in env_str
    assert str(dummy_config) in env_str

    # Ensure no private attributes are included
    assert '_orig_stderr' not in env_str
    assert '_devnull' not in env_str
