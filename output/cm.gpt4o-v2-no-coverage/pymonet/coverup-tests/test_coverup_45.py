# file: pymonet/lazy.py:50-54
# asked: {"lines": [50, 51, 52, 54], "branches": []}
# gained: {"lines": [50, 51, 52, 54], "branches": []}

import pytest
from unittest.mock import Mock
from pymonet.lazy import Lazy

def test_lazy_compute_value():
    mock_constructor = Mock(return_value=42)
    lazy_instance = Lazy(mock_constructor)
    
    result = lazy_instance._compute_value(1, 2, 3)
    
    assert lazy_instance.is_evaluated == True
    assert lazy_instance.value == 42
    assert result == 42
    mock_constructor.assert_called_once_with(1, 2, 3)
