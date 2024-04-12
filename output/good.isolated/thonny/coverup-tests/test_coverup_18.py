# file thonny/roughparse.py:654-656
# lines [654, 655, 656]
# branches []

import pytest
from thonny.roughparse import RoughParser

# Test function to improve coverage
def test_get_last_stmt_bracketing(mocker):
    # Arrange
    # Assuming RoughParser requires 'indent_width' and 'tabwidth' as arguments for initialization
    parser = RoughParser(indent_width=4, tabwidth=4)
    mocker.patch.object(parser, '_study2')  # Mock _study2 to not do any actual work
    parser.stmt_bracketing = [(0, 0)]  # Set the expected value for stmt_bracketing

    # Act
    result = parser.get_last_stmt_bracketing()

    # Assert
    assert result == [(0, 0)], "get_last_stmt_bracketing should return the correct bracketing"
