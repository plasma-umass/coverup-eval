# file: flutils/txtutils.py:233-237
# asked: {"lines": [233, 234, 235, 236, 237], "branches": [[236, 0], [236, 237]]}
# gained: {"lines": [233, 234, 235, 236, 237], "branches": [[236, 0], [236, 237]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

@pytest.fixture
def wrapper():
    return AnsiTextWrapper()

def test_subsequent_indent_setter(wrapper):
    # Set the subsequent_indent and check if it is set correctly
    wrapper.subsequent_indent = '  '
    assert wrapper._AnsiTextWrapper__subsequent_indent == '  '
    
    # Check if 'subsequent_indent_len' is deleted from __dict__ if it exists
    wrapper.__dict__['subsequent_indent_len'] = 4
    wrapper.subsequent_indent = '    '
    assert 'subsequent_indent_len' not in wrapper.__dict__

def test_subsequent_indent_setter_no_subsequent_indent_len(wrapper):
    # Ensure 'subsequent_indent_len' is not in __dict__ initially
    if 'subsequent_indent_len' in wrapper.__dict__:
        del wrapper.__dict__['subsequent_indent_len']
    
    # Set the subsequent_indent and check if it is set correctly
    wrapper.subsequent_indent = '  '
    assert wrapper._AnsiTextWrapper__subsequent_indent == '  '
    assert 'subsequent_indent_len' not in wrapper.__dict__
