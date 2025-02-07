# file: lib/ansible/plugins/filter/core.py:220-237
# asked: {"lines": [222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237], "branches": [[222, 223], [222, 225], [226, 227], [226, 232], [227, 228], [227, 229], [229, 230], [229, 231], [232, 233], [232, 237], [233, 234], [233, 235]]}
# gained: {"lines": [222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237], "branches": [[222, 223], [222, 225], [226, 227], [226, 232], [227, 228], [227, 229], [229, 230], [229, 231], [232, 233], [232, 237], [233, 234], [233, 235]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import rand
from random import Random, SystemRandom
from jinja2 import Environment

def test_rand_with_seed():
    env = Environment()
    result = rand(env, 10, seed=42)
    assert isinstance(result, int)
    assert 0 <= result < 10

def test_rand_without_seed():
    env = Environment()
    result = rand(env, 10)
    assert isinstance(result, int)
    assert 0 <= result < 10

def test_rand_with_start_and_step():
    env = Environment()
    result = rand(env, 10, start=1, step=2)
    assert isinstance(result, int)
    assert 1 <= result < 10
    assert (result - 1) % 2 == 0

def test_rand_with_iterable():
    env = Environment()
    result = rand(env, [1, 2, 3, 4, 5])
    assert result in [1, 2, 3, 4, 5]

def test_rand_with_iterable_and_start_raises_error():
    env = Environment()
    with pytest.raises(AnsibleFilterError, match="start and step can only be used with integer values"):
        rand(env, [1, 2, 3, 4, 5], start=1)

def test_rand_with_iterable_and_step_raises_error():
    env = Environment()
    with pytest.raises(AnsibleFilterError, match="start and step can only be used with integer values"):
        rand(env, [1, 2, 3, 4, 5], step=1)

def test_rand_with_invalid_type_raises_error():
    env = Environment()
    with pytest.raises(AnsibleFilterError, match="random can only be used on sequences and integers"):
        rand(env, 10.5)
