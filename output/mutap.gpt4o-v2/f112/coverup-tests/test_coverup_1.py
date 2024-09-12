# file: f112/__init__.py:1-4
# asked: {"lines": [1, 3, 4], "branches": []}
# gained: {"lines": [1, 3, 4], "branches": []}

import pytest
from f112 import reverse_delete

def test_reverse_delete():
    # Test case where characters to delete are present in the string
    s, c = "hello world", "lo"
    result = reverse_delete(s, c)
    assert result == ("he wrd", False)
    
    # Test case where no characters are deleted
    s, c = "hello", ""
    result = reverse_delete(s, c)
    assert result == ("hello", False)
    
    # Test case where the result is a palindrome
    s, c = "abccba", "d"
    result = reverse_delete(s, c)
    assert result == ("abccba", True)
    
    # Test case where all characters are deleted
    s, c = "hello", "helo"
    result = reverse_delete(s, c)
    assert result == ("", True)
    
    # Test case where input string is empty
    s, c = "", "a"
    result = reverse_delete(s, c)
    assert result == ("", True)
