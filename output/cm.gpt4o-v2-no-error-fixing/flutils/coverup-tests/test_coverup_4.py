# file: flutils/txtutils.py:255-259
# asked: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}
# gained: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_placeholder_len_with_non_empty_placeholder():
    wrapper = AnsiTextWrapper(placeholder=" [...]")
    assert wrapper.placeholder_len == 6

def test_placeholder_len_with_empty_placeholder():
    wrapper = AnsiTextWrapper(placeholder=" ")
    assert wrapper.placeholder_len == 0
