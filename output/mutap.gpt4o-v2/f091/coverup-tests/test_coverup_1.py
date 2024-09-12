# file: f091/__init__.py:1-5
# asked: {"lines": [1, 3, 4, 5], "branches": []}
# gained: {"lines": [1, 3, 4, 5], "branches": []}

import pytest
from f091 import is_bored

def test_is_bored():
    # Test case to cover the import and re.split
    S = "I am bored. You are not. I am still bored!"
    result = is_bored(S)
    assert result == 2

    # Test case to cover the scenario where no sentence starts with 'I '
    S = "You are not bored. They are not bored either."
    result = is_bored(S)
    assert result == 0

    # Test case to cover the scenario where all sentences start with 'I '
    S = "I am bored. I am still bored. I will always be bored."
    result = is_bored(S)
    assert result == 3

    # Test case to cover empty string
    S = ""
    result = is_bored(S)
    assert result == 0

    # Test case to cover string with no punctuation
    S = "I am bored I am still bored I will always be bored"
    result = is_bored(S)
    assert result == 1
