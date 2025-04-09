# file tornado/escape.py:178-180
# lines [178, 179, 180]
# branches []

import pytest
from tornado.escape import utf8

def test_utf8_overload():
    # Test the utf8 function with a string input
    input_str = "test"
    expected_output = b"test"
    result = utf8(input_str)
    assert result == expected_output

    # Test the utf8 function with a non-string input to ensure it raises an error
    with pytest.raises(TypeError):
        utf8(123)

