# file cookiecutter/prompt.py:35-41
# lines [35, 41]
# branches []

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

# Assuming the function read_repo_password is imported from cookiecutter.prompt
from cookiecutter.prompt import read_repo_password

def test_read_repo_password(mocker):
    question = "Enter your password"
    expected_password = "secret_password"
    
    # Mocking click.prompt to return a predefined password
    mocker.patch('click.prompt', return_value=expected_password)
    
    # Call the function
    result = read_repo_password(question)
    
    # Assert that the result is as expected
    assert result == expected_password
    
    # Assert that click.prompt was called with the correct parameters
    click.prompt.assert_called_once_with(question, hide_input=True)
