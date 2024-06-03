# file mimesis/providers/choice.py:20-26
# lines [20, 26]
# branches []

import pytest
from mimesis.providers.choice import Choice
from mimesis.providers.base import BaseProvider

def test_choice_initialization(mocker):
    # Mock the BaseProvider's __init__ method to ensure it is called
    mocker.patch.object(BaseProvider, '__init__', return_value=None)
    
    # Create an instance of Choice with some arguments
    args = ('arg1', 'arg2')
    kwargs = {'key1': 'value1', 'key2': 'value2'}
    choice_instance = Choice(*args, **kwargs)
    
    # Assert that the BaseProvider's __init__ method was called with the correct arguments
    BaseProvider.__init__.assert_called_once_with(*args, **kwargs)
    
    # Clean up by stopping the patch
    mocker.stopall()
