# file: string_utils/validation.py:451-494
# asked: {"lines": [451, 471, 472, 474, 475, 477, 483, 484, 485, 487, 488, 489, 491, 492, 494], "branches": [[471, 472], [471, 474], [474, 475], [474, 477], [483, 484], [483, 494], [487, 488], [487, 491], [491, 483], [491, 492]]}
# gained: {"lines": [451, 471, 472, 474, 475, 477, 483, 484, 485, 487, 488, 489, 491, 492, 494], "branches": [[471, 472], [471, 474], [474, 475], [474, 477], [483, 484], [483, 494], [487, 488], [487, 491], [491, 483], [491, 492]]}

import pytest
from string_utils.validation import is_palindrome
from string_utils._regex import SPACES_RE
from string_utils.validation import is_full_string

def test_is_palindrome():
    # Test cases where input is not a full string
    assert not is_palindrome(None)
    assert not is_palindrome('')
    assert not is_palindrome(' ')
    
    # Test cases where input is a palindrome
    assert is_palindrome('LOL')
    assert not is_palindrome('Lol')
    assert is_palindrome('Lol', ignore_case=True)
    assert is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=True)
    
    # Test cases where input is not a palindrome
    assert not is_palindrome('ROTFL')
    assert not is_palindrome('Hello')
    
    # Test cases with ignore_spaces
    assert is_palindrome('A man a plan a canal Panama', ignore_spaces=True, ignore_case=True)
    assert not is_palindrome('A man a plan a canal Panama')
    
    # Test cases with ignore_case
    assert is_palindrome('Madam', ignore_case=True)
    assert not is_palindrome('Madam')
    
    # Test cases with both ignore_spaces and ignore_case
    assert is_palindrome('A Santa at NASA', ignore_spaces=True, ignore_case=True)
    assert not is_palindrome('A Santa at NASA', ignore_spaces=True)
    assert not is_palindrome('A Santa at NASA', ignore_case=True)

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Cleanup or reset any state if necessary
    yield
    # No specific cleanup required for this test

