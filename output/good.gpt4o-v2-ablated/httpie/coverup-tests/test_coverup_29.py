# file: httpie/context.py:99-100
# asked: {"lines": [99, 100], "branches": []}
# gained: {"lines": [99, 100], "branches": []}

import pytest

from httpie.context import Environment

@pytest.fixture
def environment():
    return Environment()

def test_environment_repr(environment):
    repr_str = repr(environment)
    assert repr_str.startswith('<Environment ')
    assert repr_str.endswith('>')
    assert 'Environment' in repr_str
