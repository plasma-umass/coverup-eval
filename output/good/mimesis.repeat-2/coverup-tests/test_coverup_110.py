# file mimesis/providers/choice.py:20-26
# lines [20, 26]
# branches []

import pytest
from mimesis.providers.choice import Choice

def test_choice_initialization(mocker):
    # Mock the super().__init__ call to ensure isolation
    init_mock = mocker.patch('mimesis.providers.BaseProvider.__init__')

    # Create an instance of Choice to trigger __init__
    choice_instance = Choice('arg1', 'arg2', key1='value1', key2='value2')

    # Assert that the mocked __init__ was called with the correct arguments
    init_mock.assert_called_once_with('arg1', 'arg2', key1='value1', key2='value2')
