# file: cookiecutter/prompt.py:35-41
# asked: {"lines": [35, 41], "branches": []}
# gained: {"lines": [35, 41], "branches": []}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

from cookiecutter.prompt import read_repo_password

@pytest.fixture
def runner():
    return CliRunner()

def test_read_repo_password(runner, monkeypatch):
    # Mock the click.prompt function to simulate user input
    with patch('click.prompt', return_value='mocked_password') as mock_prompt:
        question = "Enter your password"
        result = read_repo_password(question)
        
        # Assert that the prompt was called with the correct parameters
        mock_prompt.assert_called_once_with(question, hide_input=True)
        
        # Assert that the result is as expected
        assert result == 'mocked_password'
