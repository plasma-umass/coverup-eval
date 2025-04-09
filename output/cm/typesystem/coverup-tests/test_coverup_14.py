# file typesystem/tokenize/tokenize_json.py:98-155
# lines [98, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 150, 151, 153, 155]
# branches ['116->117', '116->119', '119->120', '119->124', '124->125', '124->127', '127->128', '127->130', '130->131', '130->133', '133->134', '133->137', '138->139', '138->147', '140->141', '140->143']

import pytest
from typesystem.tokenize.tokenize_json import _make_scanner, Token, ScalarToken, DictToken, ListToken
import re
import typing

NUMBER_RE = re.compile(
    r"(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?",
    (re.VERBOSE | re.MULTILINE | re.DOTALL),
)

class MockContext:
    def __init__(self, strict=True, memo=None):
        self.strict = strict
        self.memo = memo or {}

    def parse_array(self, args, scan_once):
        string, idx = args
        return [], idx

    def parse_string(self, string, idx, strict):
        return 'string', idx + len('string') + 2

    def parse_float(self, value):
        return float(value)

    def parse_int(self, value):
        return int(value)

@pytest.fixture
def mock_context():
    return MockContext()

@pytest.fixture
def scan_once(mock_context):
    return _make_scanner(mock_context, content='')

def test_scan_once_with_number(mock_context, scan_once):
    # Test with a float
    token, end = scan_once('3.14', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 3.14
    assert end == 4

    # Test with an integer
    token, end = scan_once('42', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 42
    assert end == 2

    # Test with an exponent
    token, end = scan_once('6e2', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 600.0
    assert end == 3

    # Test with a negative number
    token, end = scan_once('-7', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == -7
    assert end == 2

    # Test with a negative float
    token, end = scan_once('-8.9', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == -8.9
    assert end == 4

    # Test with a negative exponent
    token, end = scan_once('-1e-3', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == -0.001
    assert end == 5

    # Test with a positive exponent
    token, end = scan_once('1e+3', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 1000.0
    assert end == 4

    # Test with a zero
    token, end = scan_once('0', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 0
    assert end == 1

    # Test with a zero before a dot
    token, end = scan_once('0.123', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 0.123
    assert end == 5

    # Test with a zero before an exponent
    token, end = scan_once('0e0', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 0.0
    assert end == 3

    # Test with a zero before a negative exponent
    token, end = scan_once('0e-1', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 0.0
    assert end == 4

    # Test with a zero before a positive exponent
    token, end = scan_once('0e+1', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 0.0
    assert end == 4

    # Test with a non-number to trigger StopIteration
    with pytest.raises(StopIteration):
        scan_once('a', 0)
