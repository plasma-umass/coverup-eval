# file cookiecutter/prompt.py:44-78
# lines [44, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 68, 69, 70, 71, 75, 76, 78]
# branches ['54->55', '54->57', '57->58', '57->60']

import pytest
from cookiecutter.prompt import read_user_choice
from collections import OrderedDict
import click
from click.testing import CliRunner

def test_read_user_choice_valid_input(mocker):
    mocker.patch('click.prompt', return_value='2')
    options = ['option1', 'option2', 'option3']
    result = read_user_choice('test_var', options)
    assert result == 'option2'

def test_read_user_choice_default(mocker):
    mocker.patch('click.prompt', return_value='1')
    options = ['option1', 'option2', 'option3']
    result = read_user_choice('test_var', options)
    assert result == 'option1'

def test_read_user_choice_invalid_options_type():
    with pytest.raises(TypeError):
        read_user_choice('test_var', 'not_a_list')

def test_read_user_choice_empty_options():
    with pytest.raises(ValueError):
        read_user_choice('test_var', [])

def test_read_user_choice_prompt_message(mocker):
    mock_prompt = mocker.patch('click.prompt', return_value='1')
    options = ['option1', 'option2']
    read_user_choice('test_var', options)
    expected_prompt = (
        'Select test_var:\n'
        '1 - option1\n'
        '2 - option2\n'
        'Choose from 1, 2'
    )
    # Use call_args to compare the actual call arguments
    actual_args, actual_kwargs = mock_prompt.call_args
    assert actual_args[0] == expected_prompt
    assert list(actual_kwargs['type'].choices) == ['1', '2']
    assert actual_kwargs['default'] == '1'
    assert actual_kwargs['show_choices'] is False
