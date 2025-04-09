# file mimesis/providers/choice.py:20-26
# lines [20, 26]
# branches []

import pytest
from mimesis.providers.choice import Choice

def test_choice_initialization(mocker):
    # Mock the super().__init__ call to ensure it's being called properly
    mock_super_init = mocker.patch('mimesis.providers.choice.BaseProvider.__init__', return_value=None)

    # Create an instance of Choice to trigger __init__
    args = ('arg1', 'arg2')
    kwargs = {'kwarg1': 'value1', 'kwarg2': 'value2'}
    choice_instance = Choice(*args, **kwargs)

    # Assert that the super().__init__ was called with the correct arguments
    mock_super_init.assert_called_once_with(*args, **kwargs)

    # Clean up is not necessary as the mocker fixture automatically undoes patches after the test
