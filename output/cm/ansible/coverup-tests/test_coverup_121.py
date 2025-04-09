# file lib/ansible/plugins/filter/core.py:220-237
# lines [220, 221, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237]
# branches ['222->223', '222->225', '226->227', '226->232', '227->228', '227->229', '229->230', '229->231', '232->233', '232->237', '233->234', '233->235']

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import rand
from jinja2.runtime import Context
from random import SystemRandom, Random
from unittest.mock import MagicMock

# Mocking the environment filter decorator
def environmentfilter(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Applying the mock decorator to the rand function
rand = environmentfilter(rand)

@pytest.fixture
def mock_system_random(mocker):
    mock = mocker.patch('ansible.plugins.filter.core.SystemRandom', autospec=True)
    mock_instance = mock.return_value
    mock_instance.randrange.return_value = 42
    mock_instance.choice.return_value = 'chosen'
    return mock_instance

@pytest.fixture
def mock_environment(mocker):
    environment = MagicMock()
    environment.autoescape = mocker.Mock()
    return environment

def test_rand_with_integer(mock_system_random, mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    result = rand(environment, 10)
    assert result == 42
    mock_system_random.randrange.assert_called_once_with(0, 10, 1)

def test_rand_with_iterable(mock_system_random, mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    result = rand(environment, 'abc')
    assert result == 'chosen'
    mock_system_random.choice.assert_called_once_with('abc')

def test_rand_with_integer_and_seed(mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    result = rand(environment, 10, seed=123)
    assert isinstance(result, int)

def test_rand_with_start_and_step(mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    result = rand(environment, 10, start=2, step=2)
    assert isinstance(result, int)

def test_rand_with_start_and_step_error(mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    with pytest.raises(AnsibleFilterError):
        rand(environment, 'abc', start=2)

def test_rand_with_step_error(mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    with pytest.raises(AnsibleFilterError):
        rand(environment, 'abc', step=2)

def test_rand_with_non_iterable_non_integer(mock_environment):
    environment = Context(mock_environment, {}, {}, {})
    with pytest.raises(AnsibleFilterError):
        rand(environment, 1.5)
