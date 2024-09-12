# file: cookiecutter/prompt.py:159-168
# asked: {"lines": [159, 164, 166, 167, 168], "branches": [[166, 167], [166, 168]]}
# gained: {"lines": [159, 164, 166, 167, 168], "branches": [[166, 167], [166, 168]]}

import pytest
from unittest.mock import patch, MagicMock
from cookiecutter.prompt import prompt_choice_for_config

@pytest.fixture
def mock_render_variable():
    with patch('cookiecutter.prompt.render_variable') as mock:
        yield mock

@pytest.fixture
def mock_read_user_choice():
    with patch('cookiecutter.prompt.read_user_choice') as mock:
        yield mock

def test_prompt_choice_for_config_no_input(mock_render_variable):
    cookiecutter_dict = {}
    env = MagicMock()
    key = 'key'
    options = ['option1', 'option2']
    no_input = True

    mock_render_variable.side_effect = lambda env, raw, cookiecutter_dict: raw

    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    
    assert result == 'option1'
    mock_render_variable.assert_any_call(env, 'option1', cookiecutter_dict)
    mock_render_variable.assert_any_call(env, 'option2', cookiecutter_dict)

def test_prompt_choice_for_config_with_input(mock_render_variable, mock_read_user_choice):
    cookiecutter_dict = {}
    env = MagicMock()
    key = 'key'
    options = ['option1', 'option2']
    no_input = False

    mock_render_variable.side_effect = lambda env, raw, cookiecutter_dict: raw
    mock_read_user_choice.return_value = 'option2'

    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input)
    
    assert result == 'option2'
    mock_render_variable.assert_any_call(env, 'option1', cookiecutter_dict)
    mock_render_variable.assert_any_call(env, 'option2', cookiecutter_dict)
    mock_read_user_choice.assert_called_once_with(key, ['option1', 'option2'])
