# file pysnooper/variables.py:13-17
# lines [13, 14, 15, 17]
# branches []

import pytest

def test_needs_parentheses():
    from pysnooper.variables import needs_parentheses

    # Test cases to cover different branches
    assert not needs_parentheses('a')  # No parentheses needed
    assert needs_parentheses('a + b')  # Parentheses needed
    assert not needs_parentheses('(a + b)')  # Already has parentheses
    assert not needs_parentheses('a.b')  # No parentheses needed
    assert needs_parentheses('a + b.c')  # Parentheses needed

    # Clean up if necessary (not needed in this case as no state is modified)

