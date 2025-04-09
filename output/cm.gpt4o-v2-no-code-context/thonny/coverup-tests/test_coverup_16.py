# file: thonny/roughparse.py:654-656
# asked: {"lines": [654, 655, 656], "branches": []}
# gained: {"lines": [654, 655, 656], "branches": []}

import pytest
from thonny.roughparse import RoughParser

@pytest.fixture
def rough_parser():
    return RoughParser(indent_width=4, tabwidth=4)

def test_get_last_stmt_bracketing(mocker, rough_parser):
    # Mock the _study2 method to avoid side effects
    mocker.patch.object(rough_parser, '_study2', return_value=None)
    
    # Set a value for stmt_bracketing to verify the return value
    rough_parser.stmt_bracketing = "test_bracketing"
    
    # Call the method and assert the expected return value
    result = rough_parser.get_last_stmt_bracketing()
    assert result == "test_bracketing"
