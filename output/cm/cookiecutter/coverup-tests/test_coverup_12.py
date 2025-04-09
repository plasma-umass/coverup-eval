# file cookiecutter/prompt.py:22-32
# lines [22, 32]
# branches []

import pytest
from click.testing import CliRunner
import click
from cookiecutter.prompt import read_user_yes_no

@pytest.fixture
def mock_click_prompt(mocker):
    return mocker.patch('cookiecutter.prompt.click.prompt')

def test_read_user_yes_no_with_yes_input(mock_click_prompt):
    mock_click_prompt.return_value = True
    question = "Would you like to continue?"
    default_value = False

    response = read_user_yes_no(question, default_value)

    mock_click_prompt.assert_called_once_with(question, default=default_value, type=click.BOOL)
    assert response is True

def test_read_user_yes_no_with_no_input(mock_click_prompt):
    mock_click_prompt.return_value = False
    question = "Would you like to continue?"
    default_value = True

    response = read_user_yes_no(question, default_value)

    mock_click_prompt.assert_called_once_with(question, default=default_value, type=click.BOOL)
    assert response is False
