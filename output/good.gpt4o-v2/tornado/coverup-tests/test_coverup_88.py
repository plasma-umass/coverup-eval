# file: tornado/util.py:376-382
# asked: {"lines": [376, 377, 378, 379, 380, 382], "branches": []}
# gained: {"lines": [376, 377, 378, 379, 380, 382], "branches": []}

import pytest
from tornado.util import ArgReplacer

def test_arg_replacer_init_with_positional_arg():
    def sample_func(a, b, c):
        pass

    replacer = ArgReplacer(sample_func, 'b')
    assert replacer.name == 'b'
    assert replacer.arg_pos == 1

def test_arg_replacer_init_with_non_positional_arg():
    def sample_func(a, b, c):
        pass

    replacer = ArgReplacer(sample_func, 'd')
    assert replacer.name == 'd'
    assert replacer.arg_pos is None

def test_arg_replacer_init_with_no_args():
    def sample_func():
        pass

    replacer = ArgReplacer(sample_func, 'a')
    assert replacer.name == 'a'
    assert replacer.arg_pos is None
