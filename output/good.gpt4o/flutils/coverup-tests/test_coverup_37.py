# file flutils/txtutils.py:398-412
# lines [398, 412]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_wrap():
    wrapper = AnsiTextWrapper(width=10)
    text = "This is a test string that should be wrapped."
    wrapped_text = wrapper.wrap(text)
    
    # Assertions to verify the wrapping
    assert isinstance(wrapped_text, list)
    assert all(isinstance(line, str) for line in wrapped_text)
    assert all(len(line) <= 10 for line in wrapped_text)
    assert wrapped_text == ['This is a', 'test', 'string', 'that', 'should be', 'wrapped.']

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Any necessary cleanup can be done here
    yield
    # Clean up code here if needed
