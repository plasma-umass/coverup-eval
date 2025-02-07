# file: flutils/codecs/raw_utf8_escape.py:16-24
# asked: {"lines": [16, 17, 18, 19, 20, 21, 22, 23, 24], "branches": [[17, 0], [17, 18], [18, 19], [18, 21], [22, 17], [22, 23]]}
# gained: {"lines": [16, 17, 18, 19, 20, 21, 22, 23, 24], "branches": [[17, 0], [17, 18], [18, 19], [18, 21], [22, 17], [22, 23]]}

import pytest

from flutils.codecs.raw_utf8_escape import _each_utf8_hex

def test_each_utf8_hex_ascii():
    result = list(_each_utf8_hex("hello"))
    assert result == ['h', 'e', 'l', 'l', 'o']

def test_each_utf8_hex_non_ascii():
    result = list(_each_utf8_hex("你好"))
    assert result == ['\\xe4', '\\xbd', '\\xa0', '\\xe5', '\\xa5', '\\xbd']

def test_each_utf8_hex_mixed():
    result = list(_each_utf8_hex("hello 你好"))
    assert result == ['h', 'e', 'l', 'l', 'o', ' ', '\\xe4', '\\xbd', '\\xa0', '\\xe5', '\\xa5', '\\xbd']
