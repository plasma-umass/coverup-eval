# file: flutils/txtutils.py:398-412
# asked: {"lines": [398, 412], "branches": []}
# gained: {"lines": [398, 412], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

@pytest.fixture
def wrapper():
    return AnsiTextWrapper(width=10)

def test_wrap_non_empty_text(wrapper):
    text = "This is a test sentence that should be wrapped."
    expected_output = ["This is a", "test", "sentence", "that", "should be", "wrapped."]
    result = wrapper.wrap(text)
    assert result == expected_output

def test_wrap_empty_text(wrapper):
    text = ""
    expected_output = []
    result = wrapper.wrap(text)
    assert result == expected_output

def test_wrap_no_wrapping_needed(wrapper):
    wrapper.width = 50
    text = "Short text."
    expected_output = ["Short text."]
    result = wrapper.wrap(text)
    assert result == expected_output
