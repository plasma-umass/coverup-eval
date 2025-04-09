# file: tornado/util.py:399-409
# asked: {"lines": [399, 400, 406, 407, 409], "branches": [[406, 407], [406, 409]]}
# gained: {"lines": [399, 400, 406, 407, 409], "branches": [[406, 407], [406, 409]]}

import pytest
from typing import Any, Dict, Sequence
from tornado.util import ArgReplacer

def test_get_old_value_with_positional_arg():
    def dummy_func(a, b, c):
        pass

    replacer = ArgReplacer(dummy_func, 'b')
    args = (1, 2, 3)
    kwargs = {}
    assert replacer.get_old_value(args, kwargs) == 2

def test_get_old_value_with_keyword_arg():
    def dummy_func(a, b, c):
        pass

    replacer = ArgReplacer(dummy_func, 'b')
    args = (1,)
    kwargs = {'b': 2}
    assert replacer.get_old_value(args, kwargs) == 2

def test_get_old_value_with_default():
    def dummy_func(a, b, c):
        pass

    replacer = ArgReplacer(dummy_func, 'b')
    args = (1,)
    kwargs = {}
    assert replacer.get_old_value(args, kwargs, default=42) == 42

def test_replace_with_positional_arg():
    def dummy_func(a, b, c):
        pass

    replacer = ArgReplacer(dummy_func, 'b')
    args = (1, 2, 3)
    kwargs = {}
    old_value, new_args, new_kwargs = replacer.replace(42, args, kwargs)
    assert old_value == 2
    assert new_args == [1, 42, 3]
    assert new_kwargs == {}

def test_replace_with_keyword_arg():
    def dummy_func(a, b, c):
        pass

    replacer = ArgReplacer(dummy_func, 'b')
    args = (1,)
    kwargs = {'b': 2}
    old_value, new_args, new_kwargs = replacer.replace(42, args, kwargs)
    assert old_value == 2
    assert new_args == (1,)
    assert new_kwargs == {'b': 42}

def test_replace_with_new_keyword_arg():
    def dummy_func(a, b, c):
        pass

    replacer = ArgReplacer(dummy_func, 'b')
    args = (1,)
    kwargs = {}
    old_value, new_args, new_kwargs = replacer.replace(42, args, kwargs)
    assert old_value is None
    assert new_args == (1,)
    assert new_kwargs == {'b': 42}
