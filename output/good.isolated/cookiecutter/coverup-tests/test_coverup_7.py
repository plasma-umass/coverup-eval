# file cookiecutter/prompt.py:12-19
# lines [12, 19]
# branches []

import pytest
from cookiecutter.prompt import read_user_variable
from click.testing import CliRunner

@pytest.fixture
def mock_click_prompt(mocker):
    return mocker.patch('cookiecutter.prompt.click.prompt')

def test_read_user_variable_with_input(mock_click_prompt):
    mock_click_prompt.return_value = 'user input'
    result = read_user_variable('test_var', 'default_value')
    mock_click_prompt.assert_called_once_with('test_var', default='default_value')
    assert result == 'user input'

def test_read_user_variable_with_default(mock_click_prompt):
    mock_click_prompt.return_value = 'default_value'
    result = read_user_variable('test_var', 'default_value')
    mock_click_prompt.assert_called_once_with('test_var', default='default_value')
    assert result == 'default_value'
