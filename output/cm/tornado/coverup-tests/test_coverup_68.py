# file tornado/util.py:411-432
# lines [411, 423, 425, 426, 427, 430, 431, 432]
# branches ['423->425', '423->430']

import pytest
from tornado.util import ArgReplacer

@pytest.fixture
def arg_replacer():
    class MockArgReplacer(ArgReplacer):
        def __init__(self, name, arg_pos):
            self.name = name
            self.arg_pos = arg_pos
    return MockArgReplacer

def test_arg_replacer_positional(arg_replacer):
    replacer = arg_replacer('arg', 0)
    args = ('old_value',)
    kwargs = {}
    new_value = 'new_value'
    
    old_value, new_args, new_kwargs = replacer.replace(new_value, args, kwargs)
    
    assert old_value == 'old_value'
    assert new_args == ['new_value']  # Corrected to list
    assert new_kwargs == {}

def test_arg_replacer_keyword(arg_replacer):
    replacer = arg_replacer('arg', None)
    args = ()
    kwargs = {'arg': 'old_value'}
    new_value = 'new_value'
    
    old_value, new_args, new_kwargs = replacer.replace(new_value, args, kwargs)
    
    assert old_value == 'old_value'
    assert new_args == ()
    assert new_kwargs == {'arg': 'new_value'}

def test_arg_replacer_missing(arg_replacer):
    replacer = arg_replacer('arg', None)
    args = ()
    kwargs = {}
    new_value = 'new_value'
    
    old_value, new_args, new_kwargs = replacer.replace(new_value, args, kwargs)
    
    assert old_value is None
    assert new_args == ()
    assert new_kwargs == {'arg': 'new_value'}
