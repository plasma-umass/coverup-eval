# file tornado/util.py:376-382
# lines [376, 377, 378, 379, 380, 382]
# branches []

import pytest
from unittest.mock import Mock
from tornado.util import ArgReplacer

def test_arg_replacer_positional():
    def sample_func(a, b, c):
        pass

    replacer = ArgReplacer(sample_func, 'b')
    assert replacer.name == 'b'
    assert replacer.arg_pos == 1

def test_arg_replacer_non_positional():
    def sample_func(a, b, c):
        pass

    replacer = ArgReplacer(sample_func, 'd')
    assert replacer.name == 'd'
    assert replacer.arg_pos is None
