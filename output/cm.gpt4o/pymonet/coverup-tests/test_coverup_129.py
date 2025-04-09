# file pymonet/lazy.py:139-149
# lines [147, 149]
# branches []

import pytest
from unittest.mock import Mock, patch
from pymonet.lazy import Lazy
from pymonet import monad_try

def test_lazy_to_try_executes_missing_lines():
    mock_constructor_fn = Mock()
    mock_constructor_fn.return_value = "success"
    
    lazy_instance = Lazy(mock_constructor_fn)
    
    with patch('pymonet.monad_try.Try') as mock_try:
        result = lazy_instance.to_try("arg1", "arg2")
        
        mock_try.of.assert_called_once_with(mock_constructor_fn, "arg1", "arg2")
        assert result == mock_try.of.return_value
