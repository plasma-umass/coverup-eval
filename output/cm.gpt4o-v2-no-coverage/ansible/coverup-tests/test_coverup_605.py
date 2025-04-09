# file: lib/ansible/utils/helpers.py:25-34
# asked: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}
# gained: {"lines": [25, 30, 31, 32, 34], "branches": [[30, 31], [30, 34]]}

import pytest
from ansible.utils.helpers import pct_to_int
from ansible.module_utils.six import string_types

def test_pct_to_int_with_percentage():
    assert pct_to_int("50%", 200) == 100
    assert pct_to_int("0%", 200) == 1  # min_value should be returned

def test_pct_to_int_with_integer_string():
    assert pct_to_int("42", 200) == 42

def test_pct_to_int_with_integer():
    assert pct_to_int(42, 200) == 42

def test_pct_to_int_with_min_value():
    assert pct_to_int("0%", 200, min_value=5) == 5

def test_pct_to_int_with_non_string_non_integer():
    with pytest.raises(TypeError):
        pct_to_int([], 200)

@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch):
    # Setup: Ensure no state pollution
    yield
    # Teardown: Clean up any state if necessary
