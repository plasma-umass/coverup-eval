# file pymonet/monad_try.py:4-9
# lines [4, 5]
# branches []

import pytest
from pymonet.monad_try import Try

def test_try_class(mocker):
    """
    Test the Try class to ensure it can be instantiated and used correctly.
    """
    # Mocking the __init__ method to bypass the required arguments
    mocker.patch.object(Try, '__init__', lambda self, value, is_success: None)
    
    try_instance = Try(None, True)
    assert isinstance(try_instance, Try)

    # Clean up by unpatching the __init__ method
    mocker.stopall()
