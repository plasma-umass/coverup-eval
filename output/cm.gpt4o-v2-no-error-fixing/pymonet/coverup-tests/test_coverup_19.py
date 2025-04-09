# file: pymonet/lazy.py:95-104
# asked: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}
# gained: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}

import pytest
from pymonet.lazy import Lazy

def test_lazy_get_not_evaluated(monkeypatch):
    # Arrange
    def mock_compute_value(*args):
        return "computed_value"
    
    lazy_instance = Lazy(lambda x: x)
    monkeypatch.setattr(lazy_instance, '_compute_value', mock_compute_value)
    
    # Act
    result = lazy_instance.get()
    
    # Assert
    assert result == "computed_value"
    assert lazy_instance.is_evaluated is False

def test_lazy_get_already_evaluated(monkeypatch):
    # Arrange
    lazy_instance = Lazy(lambda x: x)
    lazy_instance.is_evaluated = True
    lazy_instance.value = "memoized_value"
    
    # Act
    result = lazy_instance.get()
    
    # Assert
    assert result == "memoized_value"
    assert lazy_instance.is_evaluated is True
