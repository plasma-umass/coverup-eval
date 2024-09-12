# file: f006/__init__.py:4-18
# asked: {"lines": [4, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}
# gained: {"lines": [4, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18], "branches": [[9, 10], [9, 16], [10, 11], [10, 14]]}

import pytest
from f006 import parse_nested_parens

def test_parse_nested_parens():
    # Test with a single group of parentheses
    result = parse_nested_parens("(())")
    assert result == [2], f"Expected [2], but got {result}"

    # Test with multiple groups of parentheses
    result = parse_nested_parens("(()) () ((()))")
    assert result == [2, 1, 3], f"Expected [2, 1, 3], but got {result}"

    # Test with no parentheses
    result = parse_nested_parens("")
    assert result == [], f"Expected [], but got {result}"

    # Test with nested and non-nested groups
    result = parse_nested_parens("() (()) ((()))")
    assert result == [1, 2, 3], f"Expected [1, 2, 3], but got {result}"

    # Test with uneven parentheses
    result = parse_nested_parens("(())) ((())")
    assert result == [2, 3], f"Expected [2, 3], but got {result}"
