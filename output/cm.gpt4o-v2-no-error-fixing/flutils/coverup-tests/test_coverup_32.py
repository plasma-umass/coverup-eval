# file: flutils/txtutils.py:398-412
# asked: {"lines": [398, 412], "branches": []}
# gained: {"lines": [398, 412], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_wrap():
    wrapper = AnsiTextWrapper(width=10)
    text = "This is a test text that should be wrapped."

    # Test wrapping functionality
    wrapped_text = wrapper.wrap(text)
    assert wrapped_text == ['This is a', 'test text', 'that', 'should be', 'wrapped.']

    # Test empty text
    empty_text = ""
    wrapped_empty_text = wrapper.wrap(empty_text)
    assert wrapped_empty_text == []

    # Test text with no wrapping needed
    short_text = "Short"
    wrapped_short_text = wrapper.wrap(short_text)
    assert wrapped_short_text == ['Short']
