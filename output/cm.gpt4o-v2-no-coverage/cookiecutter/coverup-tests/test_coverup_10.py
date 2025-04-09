# file: cookiecutter/prompt.py:12-19
# asked: {"lines": [12, 19], "branches": []}
# gained: {"lines": [12, 19], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_variable

def test_read_user_variable(monkeypatch):
    runner = CliRunner()

    # Test case where user provides input
    with runner.isolated_filesystem():
        monkeypatch.setattr('click.termui.visible_prompt_func', lambda _: 'user_input')
        result = read_user_variable('var_name', 'default_value')
        assert result == 'user_input'

    # Test case where user does not provide input and default is used
    with runner.isolated_filesystem():
        monkeypatch.setattr('click.termui.visible_prompt_func', lambda _: '')
        result = read_user_variable('var_name', 'default_value')
        assert result == 'default_value'
