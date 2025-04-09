# file: cookiecutter/prompt.py:35-41
# asked: {"lines": [35, 41], "branches": []}
# gained: {"lines": [35, 41], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_repo_password

def test_read_repo_password(monkeypatch):
    # Mock the click.prompt function to return a predefined password
    monkeypatch.setattr('click.prompt', lambda x, hide_input: 'mocked_password')
    
    question = "Enter your password"
    result = read_repo_password(question)
    
    # Assert that the result is the mocked password
    assert result == 'mocked_password'
