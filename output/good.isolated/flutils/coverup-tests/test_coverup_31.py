# file flutils/txtutils.py:414-423
# lines [414, 423]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansitextwrapper_fill():
    wrapper = AnsiTextWrapper(width=10)
    text = "This is a long line that should be wrapped into a shorter one."
    expected = "This is a\nlong line\nthat\nshould be\nwrapped\ninto a\nshorter\none."
    result = wrapper.fill(text)
    assert result == expected, "AnsiTextWrapper.fill did not wrap text as expected."
