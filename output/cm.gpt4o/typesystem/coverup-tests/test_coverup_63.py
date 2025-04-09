# file typesystem/tokenize/tokenize_json.py:98-155
# lines [98, 101, 102, 103, 104, 105, 106, 107, 108, 110, 111, 112, 113, 114, 116, 117, 118, 119, 120, 121, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 143, 144, 145, 147, 149, 150, 151, 153, 155]
# branches ['116->117', '116->119', '119->120', '119->124', '124->125', '124->127', '127->128', '127->130', '130->131', '130->133', '133->134', '133->137', '138->139', '138->147', '140->141', '140->143']

import pytest
from typesystem.tokenize.tokenize_json import _make_scanner, ScalarToken, DictToken, ListToken
from unittest.mock import Mock

def test_make_scanner():
    context = Mock()
    context.parse_array = Mock(return_value=([], 2))
    context.parse_string = Mock(return_value=("string", 8))
    context.strict = True
    context.parse_float = float
    context.parse_int = int
    context.memo = {}
    
    scanner = _make_scanner(context, "test_content")
    
    # Test string parsing
    token, end = scanner('"string"', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == "string"
    assert end == 8
    
    # Test object parsing
    context.parse_object = Mock(return_value=({}, 2))
    token, end = scanner('{}', 0)
    assert isinstance(token, DictToken)
    assert token.value == {}
    assert end == 2
    
    # Test array parsing
    token, end = scanner('[1, 2, 3]', 0)
    assert isinstance(token, ListToken)
    assert token.value == []
    assert end == 2
    
    # Test null parsing
    token, end = scanner('null', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is None
    assert end == 4
    
    # Test true parsing
    token, end = scanner('true', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is True
    assert end == 4
    
    # Test false parsing
    token, end = scanner('false', 0)
    assert isinstance(token, ScalarToken)
    assert token.value is False
    assert end == 5
    
    # Test number parsing
    token, end = scanner('123', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 123
    assert end == 3
    
    token, end = scanner('123.45', 0)
    assert isinstance(token, ScalarToken)
    assert token.value == 123.45
    assert end == 6
    
    # Test StopIteration for invalid input
    with pytest.raises(StopIteration):
        scanner('invalid', 0)
