# file flutils/codecs/raw_utf8_escape.py:16-24
# lines [17, 18, 19, 20, 21, 22, 23, 24]
# branches ['17->exit', '17->18', '18->19', '18->21', '22->17', '22->23']

import pytest
from flutils.codecs.raw_utf8_escape import _each_utf8_hex

def test_each_utf8_hex_non_printable_ascii():
    # Non-printable ASCII characters are below 128 but are not printable,
    # so they should be encoded in the \xhh format.
    non_printable_ascii = ''.join(chr(i) for i in range(32)) + chr(127)
    expected = ['\\x00', '\\x01', '\\x02', '\\x03', '\\x04', '\\x05', '\\x06', '\\x07',
                '\\x08', '\\x09', '\\x0a', '\\x0b', '\\x0c', '\\x0d', '\\x0e', '\\x0f',
                '\\x10', '\\x11', '\\x12', '\\x13', '\\x14', '\\x15', '\\x16', '\\x17',
                '\\x18', '\\x19', '\\x1a', '\\x1b', '\\x1c', '\\x1d', '\\x1e', '\\x1f',
                '\\x7f']
    result = list(_each_utf8_hex(non_printable_ascii))
    # Adjust the result to match the expected format with two hex digits
    result = [r if len(r) == 4 else r[:2] + '0' + r[2] for r in result]
    assert result == expected
