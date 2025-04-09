# file: flutils/txtutils.py:217-221
# asked: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}
# gained: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_initial_indent_setter():
    wrapper = AnsiTextWrapper()
    
    # Set initial_indent to trigger the setter
    wrapper.initial_indent = "test"
    
    # Verify that the initial_indent was set correctly
    assert wrapper._AnsiTextWrapper__initial_indent == "test"
    
    # Set initial_indent_len in the __dict__ to test its deletion
    wrapper.__dict__['initial_indent_len'] = 4
    wrapper.initial_indent = "new_test"
    
    # Verify that initial_indent_len is deleted from __dict__
    assert 'initial_indent_len' not in wrapper.__dict__
