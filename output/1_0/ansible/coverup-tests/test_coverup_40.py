# file lib/ansible/utils/sentinel.py:9-48
# lines [9, 10]
# branches []

import pytest
from ansible.utils.sentinel import Sentinel

def test_sentinel_as_default_parameter_value(mocker):
    # Mocking print to capture its output
    mock_print = mocker.patch('builtins.print')

    def confirm_big_red_button(tristate=Sentinel):
        if tristate is Sentinel:
            print('You must explicitly press the big red button to blow up the base')
        elif tristate is True:
            print('Countdown to destruction activated')
        elif tristate is False:
            print('Countdown stopped')
        elif tristate is None:
            print('Waiting for more input')

    # Test with default parameter
    confirm_big_red_button()
    mock_print.assert_called_once_with('You must explicitly press the big red button to blow up the base')

    # Test with True
    mock_print.reset_mock()
    confirm_big_red_button(True)
    mock_print.assert_called_once_with('Countdown to destruction activated')

    # Test with False
    mock_print.reset_mock()
    confirm_big_red_button(False)
    mock_print.assert_called_once_with('Countdown stopped')

    # Test with None
    mock_print.reset_mock()
    confirm_big_red_button(None)
    mock_print.assert_called_once_with('Waiting for more input')

def test_sentinel_to_mark_dict_entries(mocker):
    # Mocking print to capture its output
    mock_print = mocker.patch('builtins.print')

    values = {'one': Sentinel, 'two': Sentinel}
    defaults = {'one': 1, 'two': 2}

    # Simulate setting a new value for 'one'
    values['one'] = None

    # Check the output
    for key, value in values.items():
        if value is Sentinel:
            continue
        print('%s: %s' % (key, value))

    mock_print.assert_called_once_with('one: None')
