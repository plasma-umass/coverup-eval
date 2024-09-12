# file: tornado/util.py:399-409
# asked: {"lines": [399, 400, 406, 407, 409], "branches": [[406, 407], [406, 409]]}
# gained: {"lines": [399, 400, 406, 407, 409], "branches": [[406, 407], [406, 409]]}

import pytest
from typing import Any, Dict, Sequence
from tornado.util import ArgReplacer

def test_get_old_value_with_positional_argument():
    def dummy_func(arg1, arg2, arg3):
        pass

    replacer = ArgReplacer(dummy_func, 'arg2')
    args = (1, 2, 3)
    kwargs = {}
    old_value = replacer.get_old_value(args, kwargs, default=None)
    assert old_value == 2

def test_get_old_value_with_keyword_argument():
    def dummy_func(arg1, arg2, arg3):
        pass

    replacer = ArgReplacer(dummy_func, 'arg2')
    args = (1,)
    kwargs = {'arg2': 2}
    old_value = replacer.get_old_value(args, kwargs, default=None)
    assert old_value == 2

def test_get_old_value_with_default_value():
    def dummy_func(arg1, arg2, arg3):
        pass

    replacer = ArgReplacer(dummy_func, 'arg2')
    args = (1,)
    kwargs = {}
    old_value = replacer.get_old_value(args, kwargs, default=42)
    assert old_value == 42
