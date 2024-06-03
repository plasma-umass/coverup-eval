# file sanic/cookies.py:25-34
# lines [25, 31, 32, 34]
# branches ['31->32', '31->34']

import pytest
from sanic.cookies import _quote

def test_quote():
    # Test case where the string is None
    assert _quote(None) is None

    # Test case where the string is a legal key
    assert _quote("legal_key") == "legal_key"

    # Test case where the string needs to be quoted
    special_str = "special;str"
    expected_quoted_str = '"special\\073str"'
    assert _quote(special_str) == expected_quoted_str

    # Test case where the string contains double quotes
    double_quote_str = 'str"with"quotes'
    expected_quoted_double_quote_str = '"str\\"with\\"quotes"'
    assert _quote(double_quote_str) == expected_quoted_double_quote_str

    # Test case where the string contains backslashes
    backslash_str = "str\\with\\backslashes"
    expected_quoted_backslash_str = '"str\\\\with\\\\backslashes"'
    assert _quote(backslash_str) == expected_quoted_backslash_str
