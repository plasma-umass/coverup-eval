# file: pymonet/monad_try.py:116-128
# asked: {"lines": [126, 127, 128], "branches": [[126, 127], [126, 128]]}
# gained: {"lines": [126, 127, 128], "branches": [[126, 127], [126, 128]]}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_get_or_else_success(self, mocker):
        # Mocking a successful Try instance
        mock_try = mocker.Mock(spec=Try)
        mock_try.is_success = True
        mock_try.value = "success_value"
        
        result = Try.get_or_else(mock_try, "default_value")
        
        assert result == "success_value"

    def test_get_or_else_failure(self, mocker):
        # Mocking a failed Try instance
        mock_try = mocker.Mock(spec=Try)
        mock_try.is_success = False
        
        result = Try.get_or_else(mock_try, "default_value")
        
        assert result == "default_value"
