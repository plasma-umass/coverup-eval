# file: flutils/txtutils.py:213-215
# asked: {"lines": [213, 214, 215], "branches": []}
# gained: {"lines": [213, 214, 215], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_initial_indent():
    wrapper = AnsiTextWrapper(initial_indent=">> ")
    assert wrapper.initial_indent == ">> "
    wrapper.initial_indent = "-- "
    assert wrapper.initial_indent == "-- "

def test_ansi_text_wrapper_subsequent_indent():
    wrapper = AnsiTextWrapper(subsequent_indent=">> ")
    assert wrapper.subsequent_indent == ">> "
    wrapper.subsequent_indent = "-- "
    assert wrapper.subsequent_indent == "-- "

def test_ansi_text_wrapper_placeholder():
    wrapper = AnsiTextWrapper(placeholder=" [more]")
    assert wrapper.placeholder == " [more]"
    wrapper.placeholder = " [cont]"
    assert wrapper.placeholder == " [cont]"

def test_ansi_text_wrapper_fill():
    text = "This is a sample text that will be wrapped."
    wrapper = AnsiTextWrapper(width=10)
    wrapped_text = wrapper.fill(text)
    expected_output = "This is a\nsample\ntext that\nwill be\nwrapped."
    assert wrapped_text == expected_output

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Monkeypatch or other setup steps
    yield
    # Teardown: Clean up after tests
    monkeypatch.undo()
