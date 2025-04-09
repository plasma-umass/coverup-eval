# file: flutils/txtutils.py:233-237
# asked: {"lines": [233, 234, 235, 236, 237], "branches": [[236, 0], [236, 237]]}
# gained: {"lines": [233, 234, 235, 236, 237], "branches": [[236, 0], [236, 237]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_subsequent_indent_setter():
    wrapper = AnsiTextWrapper()
    
    # Test setting subsequent_indent when 'subsequent_indent_len' is not in __dict__
    wrapper.subsequent_indent = "  "
    assert wrapper.subsequent_indent == "  "
    assert 'subsequent_indent_len' not in wrapper.__dict__
    
    # Test setting subsequent_indent when 'subsequent_indent_len' is in __dict__
    _ = wrapper.subsequent_indent_len  # Access to create the cached property
    assert 'subsequent_indent_len' in wrapper.__dict__
    wrapper.subsequent_indent = "    "
    assert wrapper.subsequent_indent == "    "
    assert 'subsequent_indent_len' not in wrapper.__dict__
