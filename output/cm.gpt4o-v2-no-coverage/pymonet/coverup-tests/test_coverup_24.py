# file: pymonet/lazy.py:95-104
# asked: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}
# gained: {"lines": [95, 102, 103, 104], "branches": [[102, 103], [102, 104]]}

import pytest
from pymonet.lazy import Lazy

def test_lazy_get_not_evaluated(mocker):
    mock_constructor = mocker.Mock(return_value=42)
    lazy_instance = Lazy(mock_constructor)
    
    mock_compute_value = mocker.patch.object(lazy_instance, '_compute_value', return_value=42)
    
    result = lazy_instance.get()
    
    mock_compute_value.assert_called_once()
    assert result == 42
    assert lazy_instance.is_evaluated is False

def test_lazy_get_evaluated(mocker):
    mock_constructor = mocker.Mock(return_value=42)
    lazy_instance = Lazy(mock_constructor)
    lazy_instance.is_evaluated = True
    lazy_instance.value = 42
    
    mock_compute_value = mocker.patch.object(lazy_instance, '_compute_value')
    
    result = lazy_instance.get()
    
    mock_compute_value.assert_not_called()
    assert result == 42
    assert lazy_instance.is_evaluated is True
