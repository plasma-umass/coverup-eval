# file: tornado/util.py:411-432
# asked: {"lines": [411, 423, 425, 426, 427, 430, 431, 432], "branches": [[423, 425], [423, 430]]}
# gained: {"lines": [411, 423, 425, 426, 427, 430, 431, 432], "branches": [[423, 425], [423, 430]]}

import pytest
from typing import Any, Dict, Sequence, Tuple
from unittest.mock import Mock

from tornado.util import ArgReplacer

@pytest.fixture
def mock_func():
    def func(arg1, arg2, arg):
        pass
    return func

@pytest.fixture
def arg_replacer(mock_func):
    return ArgReplacer(mock_func, 'arg')

def test_replace_positional_arg(arg_replacer):
    args = (1, 2, 3)
    kwargs = {}
    new_value = 99

    old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

    assert old_value == 3
    assert new_args == [1, 2, 99]
    assert new_kwargs == {}

def test_replace_keyword_arg(arg_replacer):
    args = ()
    kwargs = {'arg': 42}
    new_value = 99

    old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

    assert old_value == 42
    assert new_args == ()
    assert new_kwargs == {'arg': 99}

def test_replace_arg_not_found(arg_replacer):
    args = ()
    kwargs = {}
    new_value = 99

    old_value, new_args, new_kwargs = arg_replacer.replace(new_value, args, kwargs)

    assert old_value is None
    assert new_args == ()
    assert new_kwargs == {'arg': 99}
