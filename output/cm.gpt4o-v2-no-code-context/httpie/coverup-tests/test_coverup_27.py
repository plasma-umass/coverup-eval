# file: httpie/context.py:88-97
# asked: {"lines": [88, 89, 90, 91, 92, 93, 94, 95, 96], "branches": []}
# gained: {"lines": [88, 89, 90, 91, 92, 93, 94, 95, 96], "branches": []}

import pytest
from httpie.context import Environment

def repr_dict(d):
    return '{' + ', '.join(f'{k}: {v}' for k, v in d.items()) + '}'

@pytest.fixture
def environment(monkeypatch):
    class MockConfig:
        pass

    class MockEnvironment(Environment):
        def __init__(self):
            self._config = MockConfig()

        @property
        def config(self):
            return self._config

    env = MockEnvironment()
    return env

def test_environment_str(environment):
    env_str = str(environment)
    assert 'config' in env_str
    assert 'MockConfig' in env_str

def test_environment_str_with_custom_attributes(environment):
    environment.custom_attr = 'custom_value'
    env_str = str(environment)
    assert 'custom_attr' in env_str
    assert 'custom_value' in env_str
