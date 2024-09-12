# file: flutils/txtutils.py:414-423
# asked: {"lines": [414, 423], "branches": []}
# gained: {"lines": [414, 423], "branches": []}

import pytest
from textwrap import TextWrapper
from flutils.txtutils import AnsiTextWrapper

@pytest.fixture
def text_wrapper():
    return AnsiTextWrapper()

def test_fill_single_paragraph(text_wrapper):
    text = "This is a single paragraph that needs to be wrapped."
    wrapped_text = text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text == text_wrapper.fill(text)

def test_fill_empty_string(text_wrapper):
    text = ""
    wrapped_text = text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text == text

def test_fill_long_paragraph(text_wrapper):
    text = "This is a very long paragraph that needs to be wrapped. " * 10
    wrapped_text = text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text != text  # Ensure wrapping occurred

def test_fill_with_newlines(text_wrapper):
    text = "This is a paragraph\nwith newlines\nthat needs to be wrapped."
    wrapped_text = text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text == text_wrapper.fill(text)
