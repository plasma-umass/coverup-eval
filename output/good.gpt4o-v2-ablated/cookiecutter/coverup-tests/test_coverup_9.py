# file: cookiecutter/prompt.py:12-19
# asked: {"lines": [19], "branches": []}
# gained: {"lines": [19], "branches": []}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

# Assuming the function is imported from the module
from cookiecutter.prompt import read_user_variable

def test_read_user_variable_with_input(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr('click.prompt', lambda var_name, default: 'user_input')
    
    result = read_user_variable('test_var', 'default_value')
    assert result == 'user_input'

def test_read_user_variable_with_default(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr('click.prompt', lambda var_name, default: default)
    
    result = read_user_variable('test_var', 'default_value')
    assert result == 'default_value'
