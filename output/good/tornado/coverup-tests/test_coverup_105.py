# file tornado/util.py:399-409
# lines [399, 400, 406, 407, 409]
# branches ['406->407', '406->409']

import pytest
from tornado.util import ArgReplacer

# Define a dummy function to use with ArgReplacer
def dummy_func(test_arg, another_arg=None):
    pass

@pytest.fixture
def arg_replacer():
    # Setup code to create an ArgReplacer instance
    replacer = ArgReplacer(dummy_func, 'test_arg')
    yield replacer
    # No teardown needed as ArgReplacer does not allocate external resources

def test_get_old_value_with_args(arg_replacer):
    args = (42,)
    kwargs = {}
    default = None
    old_value = arg_replacer.get_old_value(args, kwargs, default)
    assert old_value == 42

def test_get_old_value_with_kwargs(arg_replacer):
    args = ()
    kwargs = {'test_arg': 42}
    default = None
    old_value = arg_replacer.get_old_value(args, kwargs, default)
    assert old_value == 42

def test_get_old_value_with_default(arg_replacer):
    args = ()
    kwargs = {}
    default = 42
    old_value = arg_replacer.get_old_value(args, kwargs, default)
    assert old_value == 42

def test_get_old_value_with_missing_arg_and_no_default(arg_replacer):
    args = ()
    kwargs = {}
    old_value = arg_replacer.get_old_value(args, kwargs)
    assert old_value is None
