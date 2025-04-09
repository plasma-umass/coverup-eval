# file: flutils/txtutils.py:398-412
# asked: {"lines": [398, 412], "branches": []}
# gained: {"lines": [398, 412], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_wrap_empty_string(ansi_text_wrapper):
    result = ansi_text_wrapper.wrap("")
    assert result == []

def test_wrap_single_line(ansi_text_wrapper):
    text = "This is a single line of text."
    result = ansi_text_wrapper.wrap(text)
    assert result == [text]

def test_wrap_multiple_lines(ansi_text_wrapper):
    text = "This is a long line of text that should be wrapped into multiple lines."
    ansi_text_wrapper.width = 20
    result = ansi_text_wrapper.wrap(text)
    assert result == [
        "This is a long line",
        "of text that should",
        "be wrapped into",
        "multiple lines."
    ]

def test_wrap_with_ansi_codes(ansi_text_wrapper):
    text = "\033[1mThis is a bold text that should be wrapped.\033[0m"
    ansi_text_wrapper.width = 20
    result = ansi_text_wrapper.wrap(text)
    assert result == [
        "\033[1mThis is a bold text",
        "that should be",
        "wrapped.\033[0m"
    ]
