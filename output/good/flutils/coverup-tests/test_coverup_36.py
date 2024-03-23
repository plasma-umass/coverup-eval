# file flutils/txtutils.py:398-412
# lines [398, 412]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper(width=50)

def test_ansi_text_wrapper_wrap(ansi_text_wrapper):
    text = "This is a test string that will be wrapped by AnsiTextWrapper class to test its functionality."
    expected_wrapped_text = [
        "This is a test string that will be wrapped by",
        "AnsiTextWrapper class to test its functionality."
    ]
    wrapped_text = ansi_text_wrapper.wrap(text)
    assert wrapped_text == expected_wrapped_text, "The wrapped text does not match the expected output."
