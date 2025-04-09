# file cookiecutter/prompt.py:159-168
# lines [159, 164, 166, 167, 168]
# branches ['166->167', '166->168']

import pytest
from unittest import mock
from cookiecutter.prompt import prompt_choice_for_config

def render_variable(env, raw, cookiecutter_dict):
    return raw  # Mock implementation for testing

@mock.patch('cookiecutter.prompt.render_variable', side_effect=render_variable)
def test_prompt_choice_for_config_no_input(mock_render_variable):
    cookiecutter_dict = {}
    env = mock.Mock()
    key = 'test_key'
    options = ['option1', 'option2', 'option3']
    no_input = True

    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    
    assert result == 'option1'

@mock.patch('cookiecutter.prompt.read_user_choice')
@mock.patch('cookiecutter.prompt.render_variable', side_effect=render_variable)
def test_prompt_choice_for_config_with_input(mock_render_variable, mock_read_user_choice):
    cookiecutter_dict = {}
    env = mock.Mock()
    key = 'test_key'
    options = ['option1', 'option2', 'option3']
    no_input = False

    mock_read_user_choice.return_value = 'option2'
    
    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    
    mock_read_user_choice.assert_called_once_with(key, ['option1', 'option2', 'option3'])
    assert result == 'option2'
