# file: flutils/txtutils.py:414-423
# asked: {"lines": [423], "branches": []}
# gained: {"lines": [423], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_fill():
    text = "This is a sample text that needs to be wrapped properly by the AnsiTextWrapper class."
    wrapper = AnsiTextWrapper(width=20)
    result = wrapper.fill(text)
    expected = "This is a sample\ntext that needs to\nbe wrapped properly\nby the\nAnsiTextWrapper\nclass."
    assert result == expected

