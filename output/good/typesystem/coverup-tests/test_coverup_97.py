# file typesystem/tokenize/tokenize_json.py:98-155
# lines [113, 114, 117, 118, 120, 121, 123, 125, 126, 128, 129, 131, 132, 134, 135]
# branches ['116->117', '119->120', '124->125', '127->128', '130->131', '133->134']

import pytest
from typesystem.tokenize.tokenize_json import _make_scanner, ScalarToken, DictToken, ListToken
import re
import typing

NUMBER_RE = re.compile(
    r"(-?(?:0|[1-9]\d*))(\.\d+)?([eE][-+]?\d+)?",
    (re.VERBOSE | re.MULTILINE | re.DOTALL),
)

class MockContext:
    def __init__(self, strict=True):
        self.strict = strict
        self.memo = {}

    def parse_array(self, args, scan_once):
        string, idx = args
        return [], idx + 1

    def parse_string(self, string, idx, strict):
        return "string", idx + 7

    def parse_float(self, value):
        return float(value)

    def parse_int(self, value):
        return int(value)

@pytest.fixture
def mock_context():
    return MockContext()

@pytest.fixture
def scanner(mock_context):
    return _make_scanner(mock_context, content="")

def test_make_scanner_coverage(scanner, mock_context):
    # Test for IndexError
    with pytest.raises(StopIteration):
        scanner("", 0)

    # Test for parse_string
    token, end = scanner('"string"', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "string"
    assert end == 8

    # Test for parse_object (DictToken)
    mock_context.parse_object = lambda args, strict, scan_once, memo, content: ({}, args[1] + 1)
    token, end = scanner('{}', 0)
    assert isinstance(token, DictToken)
    assert token.value == {}
    assert end == 2

    # Test for parse_array (ListToken)
    token, end = scanner('[]', 0)
    assert isinstance(token, ListToken)
    assert token.value == []
    assert end == 2

    # Test for "null"
    token, end = scanner('null', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is None
    assert end == 4

    # Test for "true"
    token, end = scanner('true', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert end == 4

    # Test for "false"
    token, end = scanner('false', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is False
    assert end == 5
