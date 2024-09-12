# file: pymonet/lazy.py:50-54
# asked: {"lines": [50, 51, 52, 54], "branches": []}
# gained: {"lines": [50, 51, 52, 54], "branches": []}

import pytest
from unittest.mock import Mock

from pymonet.lazy import Lazy

@pytest.fixture
def lazy_instance():
    constructor_fn = Mock(return_value="computed_value")
    instance = Lazy(constructor_fn)
    return instance, constructor_fn

def test_compute_value(lazy_instance):
    instance, constructor_fn = lazy_instance
    args = (1, 2, 3)
    
    result = instance._compute_value(*args)
    
    constructor_fn.assert_called_once_with(*args)
    assert instance.is_evaluated is True
    assert instance.value == "computed_value"
    assert result == "computed_value"
