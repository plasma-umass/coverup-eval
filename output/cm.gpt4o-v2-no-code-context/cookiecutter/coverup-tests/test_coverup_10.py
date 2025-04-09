# file: cookiecutter/prompt.py:159-168
# asked: {"lines": [159, 164, 166, 167, 168], "branches": [[166, 167], [166, 168]]}
# gained: {"lines": [159, 164, 166, 167, 168], "branches": [[166, 167], [166, 168]]}

import pytest
from unittest.mock import patch, MagicMock
from cookiecutter.prompt import prompt_choice_for_config

@pytest.fixture
def cookiecutter_dict():
    return {"project_name": "test_project"}

@pytest.fixture
def env():
    mock_env = MagicMock()
    mock_env.from_string.return_value.render.return_value = "rendered_option"
    return mock_env

@pytest.fixture
def key():
    return "project_type"

@pytest.fixture
def options():
    return ["option1", "option2", "option3"]

def test_prompt_choice_for_config_no_input(cookiecutter_dict, env, key, options):
    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input=True)
    assert result == "rendered_option"

@patch('cookiecutter.prompt.read_user_choice')
def test_prompt_choice_for_config_with_input(mock_read_user_choice, cookiecutter_dict, env, key, options):
    mock_read_user_choice.return_value = "rendered_option"
    result = prompt_choice_for_config(cookiecutter_dict, env, key, options, no_input=False)
    mock_read_user_choice.assert_called_once_with(key, ["rendered_option", "rendered_option", "rendered_option"])
    assert result == "rendered_option"
