# file: pymonet/lazy.py:106-115
# asked: {"lines": [106, 113, 115], "branches": []}
# gained: {"lines": [106, 113, 115], "branches": []}

import pytest
from pymonet.lazy import Lazy
from pymonet.box import Box

class TestLazy:
    def test_to_box(self, mocker):
        # Mock the get method to control its output
        mock_get = mocker.patch.object(Lazy, 'get', return_value=42)
        
        # Create an instance of Lazy
        lazy_instance = Lazy(lambda x: x + 1)
        
        # Call the to_box method
        box_instance = lazy_instance.to_box(41)
        
        # Assert that the get method was called with the correct arguments
        mock_get.assert_called_once_with(41)
        
        # Assert that the result is a Box instance containing the expected value
        assert isinstance(box_instance, Box)
        assert box_instance.value == 42
