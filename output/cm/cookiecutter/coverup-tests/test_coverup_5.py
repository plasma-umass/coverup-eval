# file cookiecutter/prompt.py:35-41
# lines [35, 41]
# branches []

import pytest
from cookiecutter.prompt import read_repo_password
from unittest.mock import patch

def test_read_repo_password(mocker):
    # Mock the click.prompt to return a specific password without user input
    prompt_mock = mocker.patch('click.prompt', return_value='fake-password')

    # Call the function to test
    password = read_repo_password('Enter your password:')

    # Assert that the password returned is the one we mocked
    assert password == 'fake-password'

    # Assert that click.prompt was called with the correct parameters
    prompt_mock.assert_called_once_with('Enter your password:', hide_input=True)
