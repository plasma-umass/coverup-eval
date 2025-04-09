# file: cookiecutter/prompt.py:12-19
# asked: {"lines": [12, 19], "branches": []}
# gained: {"lines": [12, 19], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_variable

def test_read_user_variable_with_input(monkeypatch):
    runner = CliRunner()

    def mock_prompt(text, default):
        return "user_input"

    monkeypatch.setattr(click, 'prompt', mock_prompt)

    result = read_user_variable("var_name", "default_value")
    assert result == "user_input"

def test_read_user_variable_with_default(monkeypatch):
    runner = CliRunner()

    def mock_prompt(text, default):
        return default

    monkeypatch.setattr(click, 'prompt', mock_prompt)

    result = read_user_variable("var_name", "default_value")
    assert result == "default_value"
