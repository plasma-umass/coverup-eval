# file: flutils/txtutils.py:398-412
# asked: {"lines": [398, 412], "branches": []}
# gained: {"lines": [398, 412], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_wrap():
    wrapper = AnsiTextWrapper(width=10)
    text = "This is a test string that will be wrapped."
    
    # Test wrapping functionality
    wrapped_text = wrapper.wrap(text)
    assert wrapped_text == ['This is a', 'test', 'string', 'that will', 'be', 'wrapped.']
    
    # Test empty string
    empty_text = ""
    wrapped_empty_text = wrapper.wrap(empty_text)
    assert wrapped_empty_text == []

    # Test string with no spaces
    no_space_text = "A"*50
    wrapped_no_space_text = wrapper.wrap(no_space_text)
    assert wrapped_no_space_text == ['A'*10, 'A'*10, 'A'*10, 'A'*10, 'A'*10]

    # Test string with newlines
    newline_text = "This is a test\nstring that will be wrapped."
    wrapped_newline_text = wrapper.wrap(newline_text)
    assert wrapped_newline_text == ['This is a', 'test', 'string', 'that will', 'be', 'wrapped.']

    # Test string with tabs
    tab_text = "This is a\ttest string that will be wrapped."
    wrapped_tab_text = wrapper.wrap(tab_text)
    assert wrapped_tab_text == ['This is a', 'test', 'string', 'that will', 'be', 'wrapped.']
