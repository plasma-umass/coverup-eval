# file: flutils/txtutils.py:213-215
# asked: {"lines": [213, 214, 215], "branches": []}
# gained: {"lines": [213, 214, 215], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_initial_indent_property(ansi_text_wrapper):
    # Set the private attribute directly for testing purposes
    ansi_text_wrapper._AnsiTextWrapper__initial_indent = ">> "
    
    # Access the property to ensure it returns the correct value
    assert ansi_text_wrapper.initial_indent == ">> "
