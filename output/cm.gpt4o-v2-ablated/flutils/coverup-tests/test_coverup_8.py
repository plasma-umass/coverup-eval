# file: flutils/txtutils.py:217-221
# asked: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}
# gained: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

@pytest.fixture
def wrapper():
    return AnsiTextWrapper()

def test_initial_indent_setter(wrapper):
    # Test setting initial_indent and check if it is set correctly
    wrapper.initial_indent = "test"
    assert wrapper._AnsiTextWrapper__initial_indent == "test"
    
    # Test if 'initial_indent_len' is deleted from __dict__ if it exists
    wrapper.__dict__['initial_indent_len'] = 10
    wrapper.initial_indent = "new_test"
    assert 'initial_indent_len' not in wrapper.__dict__

def test_initial_indent_setter_no_initial_indent_len(wrapper):
    # Test setting initial_indent when 'initial_indent_len' is not in __dict__
    wrapper.initial_indent = "another_test"
    assert wrapper._AnsiTextWrapper__initial_indent == "another_test"
    assert 'initial_indent_len' not in wrapper.__dict__
