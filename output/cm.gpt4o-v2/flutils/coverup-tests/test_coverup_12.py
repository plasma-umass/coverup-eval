# file: flutils/txtutils.py:217-221
# asked: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}
# gained: {"lines": [217, 218, 219, 220, 221], "branches": [[220, 0], [220, 221]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_initial_indent_setter():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = "test"
    assert wrapper.initial_indent == "test"
    assert 'initial_indent_len' not in wrapper.__dict__

    # Access initial_indent_len to cache it
    _ = wrapper.initial_indent_len
    assert 'initial_indent_len' in wrapper.__dict__

    # Change initial_indent and check if initial_indent_len is removed
    wrapper.initial_indent = "new_test"
    assert wrapper.initial_indent == "new_test"
    assert 'initial_indent_len' not in wrapper.__dict__

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to run before each test
    yield
    # Code to run after each test
    # Clean up any state here if necessary
