# file: httpie/context.py:88-97
# asked: {"lines": [88, 89, 90, 91, 92, 93, 94, 95, 96], "branches": []}
# gained: {"lines": [88, 89, 90, 91, 92, 93, 94, 95, 96], "branches": []}

import pytest
from httpie.context import Environment
from httpie.utils import repr_dict

def test_environment_str(monkeypatch):
    # Mock the config property to avoid dependency on actual config
    class MockConfig:
        pass

    monkeypatch.setattr(Environment, 'config', MockConfig())

    env = Environment()
    env_str = str(env)
    
    # Ensure that the string representation includes the 'config' key
    assert 'config' in env_str

    # Ensure that the string representation does not include private attributes
    assert '_orig_stderr' not in env_str
    assert '_devnull' not in env_str
