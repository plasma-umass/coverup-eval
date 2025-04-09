# file: cookiecutter/prompt.py:22-32
# asked: {"lines": [22, 32], "branches": []}
# gained: {"lines": [22, 32], "branches": []}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

# Assuming the function read_user_yes_no is imported from cookiecutter.prompt
from cookiecutter.prompt import read_user_yes_no

@pytest.fixture
def runner():
    return CliRunner()

def test_read_user_yes_no_default_yes(runner, monkeypatch):
    monkeypatch.setattr('click.prompt', lambda q, default, type: default)
    result = read_user_yes_no("Do you want to continue?", True)
    assert result is True

def test_read_user_yes_no_default_no(runner, monkeypatch):
    monkeypatch.setattr('click.prompt', lambda q, default, type: default)
    result = read_user_yes_no("Do you want to continue?", False)
    assert result is False

def test_read_user_yes_no_yes_input(runner, monkeypatch):
    monkeypatch.setattr('click.prompt', lambda q, default, type: True)
    result = read_user_yes_no("Do you want to continue?", False)
    assert result is True

def test_read_user_yes_no_no_input(runner, monkeypatch):
    monkeypatch.setattr('click.prompt', lambda q, default, type: False)
    result = read_user_yes_no("Do you want to continue?", True)
    assert result is False
