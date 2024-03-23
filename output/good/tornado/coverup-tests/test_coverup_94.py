# file tornado/util.py:376-382
# lines [376, 377, 378, 379, 380, 382]
# branches []

import pytest
from tornado.util import ArgReplacer

def test_arg_replacer():
    def sample_function(arg1, arg2):
        return arg1, arg2

    # Test with a valid positional argument name
    replacer = ArgReplacer(sample_function, 'arg1')
    assert replacer.name == 'arg1'
    assert replacer.arg_pos == 0

    # Test with a valid positional argument name that is not the first one
    replacer = ArgReplacer(sample_function, 'arg2')
    assert replacer.name == 'arg2'
    assert replacer.arg_pos == 1

    # Test with an invalid positional argument name
    replacer = ArgReplacer(sample_function, 'arg3')
    assert replacer.name == 'arg3'
    assert replacer.arg_pos is None

    # Clean up is not necessary as no external state is modified
