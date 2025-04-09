# file: cookiecutter/prompt.py:35-41
# asked: {"lines": [35, 41], "branches": []}
# gained: {"lines": [35, 41], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_repo_password

def test_read_repo_password(monkeypatch):
    # Mock the click.prompt function to simulate user input
    monkeypatch.setattr('click.prompt', lambda x, hide_input: 'mocked_password')
    
    question = "Enter your password"
    result = read_repo_password(question)
    
    assert result == 'mocked_password'
