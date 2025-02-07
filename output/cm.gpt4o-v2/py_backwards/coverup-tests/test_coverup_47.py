# file: py_backwards/utils/snippet.py:132-143
# asked: {"lines": [132], "branches": []}
# gained: {"lines": [132], "branches": []}

import pytest
from py_backwards.utils.snippet import let

def test_let_function():
    # Test the let function to ensure it executes without errors
    try:
        let("x")
    except Exception as e:
        pytest.fail(f"let() raised {type(e).__name__} unexpectedly!")

    # Since let() has no return and no side effects, we can't assert any changes
    # We just ensure it runs without errors
