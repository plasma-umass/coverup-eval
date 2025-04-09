# file: typesystem/tokenize/tokenize_json.py:98-155
# asked: {"lines": [98, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}
# gained: {"lines": [98, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 150, 151, 153, 155], "branches": [[116, 117], [116, 119], [119, 120], [119, 124], [124, 125], [124, 127], [127, 128], [127, 130], [130, 131], [130, 133], [133, 134], [133, 137], [138, 139], [138, 147], [140, 141], [140, 143]]}

import pytest
from typesystem.tokenize.tokenize_json import _make_scanner
from typesystem.tokenize.tokens import DictToken, ListToken, ScalarToken, Token

class MockContext:
    def __init__(self):
        self.parse_array = lambda x, y: ([], x[1])
        self.parse_string = lambda x, y, z: ("parsed_string", y + 12)
        self.strict = True
        self.parse_float = float
        self.parse_int = int
        self.memo = {}

def mock_parse_object(s_and_end, strict, scan_once, memo, content):
    return {}, s_and_end[1]

@pytest.fixture
def context(monkeypatch):
    context = MockContext()
    monkeypatch.setattr('typesystem.tokenize.tokenize_json._TokenizingJSONObject', mock_parse_object)
    return context

def test_scan_string(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('"string"', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "parsed_string"
    assert end == 13

def test_scan_object(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('{"key": "value"}', 0)
    assert isinstance(token, DictToken)
    assert token.value == {}
    assert end == 1

def test_scan_array(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('[]', 0)
    assert isinstance(token, ListToken)
    assert token.value == []
    assert end == 1

def test_scan_null(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('null', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is None
    assert end == 4

def test_scan_true(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('true', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert end == 4

def test_scan_false(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('false', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is False
    assert end == 5

def test_scan_number_int(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('123', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert end == 3

def test_scan_number_float(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('123.45', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 123.45
    assert end == 6

def test_scan_number_exp(context):
    scanner = _make_scanner(context, 'content')
    token, end = scanner('123e2', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 12300.0
    assert end == 5

def test_scan_invalid(context):
    scanner = _make_scanner(context, 'content')
    with pytest.raises(StopIteration):
        scanner('invalid', 0)
