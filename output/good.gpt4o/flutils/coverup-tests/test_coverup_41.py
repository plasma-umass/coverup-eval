# file flutils/codecs/raw_utf8_escape.py:16-24
# lines [16, 17, 18, 19, 20, 21, 22, 23, 24]
# branches ['17->exit', '17->18', '18->19', '18->21', '22->17', '22->23']

import pytest
from flutils.codecs.raw_utf8_escape import _each_utf8_hex

def test_each_utf8_hex():
    # Test with a mix of printable ASCII and non-ASCII characters
    text = "hello世界"
    result = list(_each_utf8_hex(text))
    expected = ['h', 'e', 'l', 'l', 'o', '\\xe4', '\\xb8', '\\x96', '\\xe7', '\\x95', '\\x8c']
    assert result == expected

    # Test with only printable ASCII characters
    text = "hello"
    result = list(_each_utf8_hex(text))
    expected = ['h', 'e', 'l', 'l', 'o']
    assert result == expected

    # Test with only non-ASCII characters
    text = "世界"
    result = list(_each_utf8_hex(text))
    expected = ['\\xe4', '\\xb8', '\\x96', '\\xe7', '\\x95', '\\x8c']
    assert result == expected

    # Test with a mix of printable and non-printable ASCII characters
    text = "hello\x00world"
    result = list(_each_utf8_hex(text))
    expected = ['h', 'e', 'l', 'l', 'o', '\\x0', 'w', 'o', 'r', 'l', 'd']
    assert result == expected

    # Test with an empty string
    text = ""
    result = list(_each_utf8_hex(text))
    expected = []
    assert result == expected
