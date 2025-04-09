# file: flutils/txtutils.py:414-423
# asked: {"lines": [414, 423], "branches": []}
# gained: {"lines": [414, 423], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

@pytest.fixture
def ansi_text_wrapper():
    wrapper = AnsiTextWrapper()
    wrapper.width = 20  # Set a width to ensure wrapping occurs
    return wrapper

def test_ansi_text_wrapper_fill(ansi_text_wrapper):
    text = "This is a sample text that needs to be wrapped."
    wrapped_text = ansi_text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text != text
    assert "\n" in wrapped_text  # Assuming the text is long enough to be wrapped

def test_ansi_text_wrapper_fill_short_text(ansi_text_wrapper):
    text = "Short text."
    wrapped_text = ansi_text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text == text  # Short text should not be wrapped

def test_ansi_text_wrapper_fill_empty_text(ansi_text_wrapper):
    text = ""
    wrapped_text = ansi_text_wrapper.fill(text)
    assert isinstance(wrapped_text, str)
    assert wrapped_text == text  # Empty text should remain empty
