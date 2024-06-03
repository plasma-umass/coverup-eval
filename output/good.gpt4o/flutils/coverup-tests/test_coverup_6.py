# file flutils/txtutils.py:217-221
# lines [217, 218, 219, 220, 221]
# branches ['220->exit', '220->221']

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_AnsiTextWrapper_initial_indent_setter():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = "test"
    
    # Verify that the initial_indent is set correctly
    assert wrapper._AnsiTextWrapper__initial_indent == "test"
    
    # Manually set initial_indent_len to simulate the condition
    wrapper.__dict__['initial_indent_len'] = 4
    
    # Change the initial_indent to trigger the deletion of initial_indent_len
    wrapper.initial_indent = "new_test"
    
    # Verify that initial_indent_len is deleted
    assert 'initial_indent_len' not in wrapper.__dict__
