# file mimesis/providers/choice.py:20-26
# lines [20, 26]
# branches []

import pytest
from mimesis.providers.choice import Choice

# Since the class Choice does not have any specific behavior in its __init__ method
# other than calling its superclass's __init__, we need to ensure that the superclass
# is properly initialized. We can mock the superclass's __init__ to assert it's called.

def test_choice_init(mocker):
    # Mock the __init__ method of the superclass
    mock_super_init = mocker.patch('mimesis.providers.base.BaseProvider.__init__')

    # Create an instance of Choice to trigger __init__
    choice = Choice('arg1', 'arg2', key1='value1', key2='value2')

    # Assert that the superclass's __init__ was called with the correct arguments
    mock_super_init.assert_called_once_with('arg1', 'arg2', key1='value1', key2='value2')

    # Clean up is not necessary as the mocker fixture automatically undoes patches
    # after the test function has completed.
