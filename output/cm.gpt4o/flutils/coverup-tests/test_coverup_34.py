# file flutils/txtutils.py:414-423
# lines [414, 423]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper

def test_ansi_text_wrapper_fill():
    wrapper = AnsiTextWrapper(width=10)
    input_text = "This is a test string that should be wrapped."
    expected_output = "This is a\ntest\nstring\nthat\nshould be\nwrapped."
    
    result = wrapper.fill(input_text)
    
    assert result == expected_output
