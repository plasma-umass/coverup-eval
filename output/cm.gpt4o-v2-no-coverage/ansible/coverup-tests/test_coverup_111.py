# file: lib/ansible/plugins/filter/core.py:220-237
# asked: {"lines": [220, 221, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237], "branches": [[222, 223], [222, 225], [226, 227], [226, 232], [227, 228], [227, 229], [229, 230], [229, 231], [232, 233], [232, 237], [233, 234], [233, 235]]}
# gained: {"lines": [220, 221, 222, 223, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 237], "branches": [[222, 223], [222, 225], [226, 227], [226, 232], [227, 228], [227, 229], [229, 230], [229, 231], [232, 233], [232, 237], [233, 234], [233, 235]]}

import pytest
from ansible.errors import AnsibleFilterError
from ansible.plugins.filter.core import rand
from jinja2 import Environment

@pytest.fixture
def environment():
    return Environment()

def test_rand_with_integer(environment):
    result = rand(environment, 10)
    assert 0 <= result < 10

def test_rand_with_integer_and_start(environment):
    result = rand(environment, 10, start=5)
    assert 5 <= result < 10

def test_rand_with_integer_start_and_step(environment):
    result = rand(environment, 10, start=2, step=2)
    assert result in [2, 4, 6, 8]

def test_rand_with_seed(environment):
    result1 = rand(environment, 10, seed=1)
    result2 = rand(environment, 10, seed=1)
    assert result1 == result2

def test_rand_with_sequence(environment):
    result = rand(environment, [1, 2, 3, 4, 5])
    assert result in [1, 2, 3, 4, 5]

def test_rand_with_sequence_and_seed(environment):
    result1 = rand(environment, [1, 2, 3, 4, 5], seed=1)
    result2 = rand(environment, [1, 2, 3, 4, 5], seed=1)
    assert result1 == result2

def test_rand_with_sequence_and_start_raises_error(environment):
    with pytest.raises(AnsibleFilterError, match='start and step can only be used with integer values'):
        rand(environment, [1, 2, 3, 4, 5], start=1)

def test_rand_with_sequence_and_step_raises_error(environment):
    with pytest.raises(AnsibleFilterError, match='start and step can only be used with integer values'):
        rand(environment, [1, 2, 3, 4, 5], step=1)

def test_rand_with_invalid_type_raises_error(environment):
    with pytest.raises(AnsibleFilterError, match='random can only be used on sequences and integers'):
        rand(environment, 10.5)
