# file flutils/txtutils.py:261-271
# lines [261, 263, 271]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper
import re
from itertools import chain

# Assuming _ANSI_RE is a regular expression defined in the flutils.txtutils module
# that matches ANSI escape codes. Since it's not provided in the question, we'll
# define a dummy pattern here for the sake of the test.
_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_ansi_text_wrapper_split(ansi_text_wrapper):
    # Test with a string that includes ANSI escape codes
    text_with_ansi = "Hello\x1b[31mRed\x1b[0mWorld"
    expected_chunks = ["Hello", "\x1b[31m", "Red", "\x1b[0m", "World"]
    
    # Call the _split method which should handle ANSI escape codes
    chunks = ansi_text_wrapper._split(text_with_ansi)
    
    # Assert that the split chunks match the expected output
    assert chunks == expected_chunks, "AnsiTextWrapper._split did not correctly split ANSI escape codes"
