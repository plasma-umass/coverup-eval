# file cookiecutter/prompt.py:159-168
# lines [159, 164, 166, 167, 168]
# branches ['166->167', '166->168']

import pytest
from cookiecutter.prompt import prompt_choice_for_config
from jinja2 import Environment

@pytest.fixture
def mock_env(mocker):
    env = mocker.Mock(spec=Environment)
    env.from_string.return_value.render.return_value = 'rendered_value'
    return env

@pytest.fixture
def mock_read_user_choice(mocker):
    return mocker.patch('cookiecutter.prompt.read_user_choice', return_value='user_choice')

def test_prompt_choice_for_config_no_input(mock_env):
    cookiecutter_dict = {}
    key = 'test_key'
    options = ['option1']
    no_input = True

    result = prompt_choice_for_config(cookiecutter_dict, mock_env, key, options, no_input)

    assert result == 'rendered_value'
    mock_env.from_string.assert_called_once_with(options[0])
    mock_env.from_string.return_value.render.assert_called_once_with(cookiecutter=cookiecutter_dict)

def test_prompt_choice_for_config_with_input(mock_env, mock_read_user_choice):
    cookiecutter_dict = {}
    key = 'test_key'
    options = ['option1', 'option2']
    no_input = False

    result = prompt_choice_for_config(cookiecutter_dict, mock_env, key, options, no_input)

    assert result == 'user_choice'
    assert mock_env.from_string.call_count == len(options)
    mock_read_user_choice.assert_called_once_with(key, ['rendered_value', 'rendered_value'])
