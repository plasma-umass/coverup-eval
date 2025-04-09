# file: httpie/context.py:122-124
# asked: {"lines": [124], "branches": []}
# gained: {"lines": [124], "branches": []}

import pytest

from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_devnull_setter(environment):
    # Set a value to devnull
    environment.devnull = 'test_value'
    
    # Assert that the value was set correctly
    assert environment._devnull == 'test_value'
