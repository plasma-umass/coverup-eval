# file: pymonet/monad_try.py:107-114
# asked: {"lines": [107, 114], "branches": []}
# gained: {"lines": [107, 114], "branches": []}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_get_success(self):
        # Create a Try instance with a value
        try_instance = Try(42, True)
        
        # Assert that get() returns the correct value
        assert try_instance.get() == 42

    def test_get_failure(self, monkeypatch):
        # Create a Try instance without setting a value
        try_instance = Try(None, False)
        
        # Monkeypatch the value attribute to simulate an AttributeError
        monkeypatch.delattr(try_instance, 'value', raising=False)
        
        # Assert that accessing get() raises an AttributeError
        with pytest.raises(AttributeError):
            try_instance.get()
