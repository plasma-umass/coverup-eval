# file: tornado/util.py:411-432
# asked: {"lines": [411, 423, 425, 426, 427, 430, 431, 432], "branches": [[423, 425], [423, 430]]}
# gained: {"lines": [411, 423, 425, 426, 427, 430, 431, 432], "branches": [[423, 425], [423, 430]]}

import pytest
from typing import Any, Dict, Sequence, Tuple
from tornado.util import ArgReplacer

def dummy_function(a, b, c=None):
    pass

@pytest.fixture
def arg_replacer():
    return ArgReplacer(dummy_function, 'b')

def test_replace_positional(arg_replacer):
    args = (1, 2, 3)
    kwargs = {}
    new_value = 99

    old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

    assert old_value == 2
    assert new_args == [1, 99, 3]  # Adjusted to list comparison
    assert new_kwargs == {}

def test_replace_keyword(arg_replacer):
    args = (1,)
    kwargs = {'b': 2, 'c': 3}
    new_value = 99

    old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

    assert old_value == 2
    assert new_args == (1,)
    assert new_kwargs == {'b': 99, 'c': 3}

def test_replace_missing_keyword(arg_replacer):
    args = (1,)
    kwargs = {'c': 3}
    new_value = 99

    old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

    assert old_value is None
    assert new_args == (1,)
    assert new_kwargs == {'c': 3, 'b': 99}
