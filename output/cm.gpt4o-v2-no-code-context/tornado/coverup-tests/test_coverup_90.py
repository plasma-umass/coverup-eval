# file: tornado/util.py:376-382
# asked: {"lines": [376, 377, 378, 379, 380, 382], "branches": []}
# gained: {"lines": [376, 377, 378, 379, 380, 382], "branches": []}

import pytest
from tornado.util import ArgReplacer

def dummy_function(a, b, c):
    return a + b + c

def dummy_function_with_kwargs(a, b, c, *, d=4):
    return a + b + c + d

def test_arg_replacer_positional():
    replacer = ArgReplacer(dummy_function, 'b')
    assert replacer.name == 'b'
    assert replacer.arg_pos == 1

def test_arg_replacer_non_positional():
    replacer = ArgReplacer(dummy_function_with_kwargs, 'd')
    assert replacer.name == 'd'
    assert replacer.arg_pos is None
