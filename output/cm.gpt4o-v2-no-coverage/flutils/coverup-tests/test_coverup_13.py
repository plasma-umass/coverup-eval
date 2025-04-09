# file: flutils/txtutils.py:255-259
# asked: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}
# gained: {"lines": [255, 256, 257, 258, 259], "branches": [[257, 258], [257, 259]]}

import pytest
from flutils.txtutils import AnsiTextWrapper, len_without_ansi

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_placeholder_len_with_non_empty_placeholder(ansi_text_wrapper):
    ansi_text_wrapper.placeholder = ' [...]'
    assert ansi_text_wrapper.placeholder_len == len_without_ansi(' [...]')

def test_placeholder_len_with_empty_placeholder(ansi_text_wrapper):
    ansi_text_wrapper.placeholder = ' '
    assert ansi_text_wrapper.placeholder_len == 0

def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
