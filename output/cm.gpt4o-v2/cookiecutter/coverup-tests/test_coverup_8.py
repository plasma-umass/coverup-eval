# file: cookiecutter/prompt.py:12-19
# asked: {"lines": [12, 19], "branches": []}
# gained: {"lines": [12, 19], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_variable

def test_read_user_variable(monkeypatch):
    runner = CliRunner()

    # Mock click.prompt to return a specific value
    monkeypatch.setattr('click.prompt', lambda x, default: 'mocked_value')

    result = read_user_variable('var_name', 'default_value')
    assert result == 'mocked_value'

    # Mock click.prompt to return the default value
    monkeypatch.setattr('click.prompt', lambda x, default: default)

    result = read_user_variable('var_name', 'default_value')
    assert result == 'default_value'
