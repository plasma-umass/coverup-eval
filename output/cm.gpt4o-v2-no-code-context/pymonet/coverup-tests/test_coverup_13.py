# file: pymonet/semigroups.py:102-117
# asked: {"lines": [102, 103, 107, 108, 110, 117], "branches": []}
# gained: {"lines": [102, 103, 107, 108, 110, 117], "branches": []}

import pytest
from pymonet.semigroups import Last

def test_last_str():
    last_instance = Last(10)
    assert str(last_instance) == 'Last[value=10]'

def test_last_concat():
    last_instance1 = Last(10)
    last_instance2 = Last(20)
    result = last_instance1.concat(last_instance2)
    assert isinstance(result, Last)
    assert result.value == 20

@pytest.fixture
def cleanup():
    # Any necessary cleanup code can be placed here
    yield
    # Cleanup actions after the test
    # For example, if there were any global state changes, revert them here

def test_last_concat_cleanup(cleanup):
    last_instance1 = Last(10)
    last_instance2 = Last(20)
    result = last_instance1.concat(last_instance2)
    assert isinstance(result, Last)
    assert result.value == 20
