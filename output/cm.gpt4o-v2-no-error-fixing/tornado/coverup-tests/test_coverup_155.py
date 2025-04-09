# file: tornado/util.py:376-382
# asked: {"lines": [380, 382], "branches": []}
# gained: {"lines": [380, 382], "branches": []}

import pytest
from tornado.util import ArgReplacer

def test_arg_replacer_init_with_value_error():
    def sample_function(a, b, c):
        pass

    replacer = ArgReplacer(sample_function, 'd')
    assert replacer.arg_pos is None

def test_arg_replacer_init_without_value_error():
    def sample_function(a, b, c):
        pass

    replacer = ArgReplacer(sample_function, 'b')
    assert replacer.arg_pos == 1
