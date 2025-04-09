# file pymonet/monad_try.py:116-128
# lines [116, 126, 127, 128]
# branches ['126->127', '126->128']

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_get_or_else_success(self, mocker):
        # Mocking a successful Try instance
        try_instance = Try.__new__(Try)
        try_instance.is_success = True
        try_instance.value = "success_value"
        
        result = try_instance.get_or_else("default_value")
        
        assert result == "success_value"

    def test_get_or_else_failure(self, mocker):
        # Mocking a failed Try instance
        try_instance = Try.__new__(Try)
        try_instance.is_success = False
        
        result = try_instance.get_or_else("default_value")
        
        assert result == "default_value"
