# file: cookiecutter/prompt.py:22-32
# asked: {"lines": [22, 32], "branches": []}
# gained: {"lines": [22, 32], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_yes_no

def test_read_user_yes_no_yes(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr('click.prompt', lambda x, default, type: True)
    result = read_user_yes_no("Do you want to continue?", True)
    assert result is True

def test_read_user_yes_no_no(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr('click.prompt', lambda x, default, type: False)
    result = read_user_yes_no("Do you want to continue?", False)
    assert result is False

def test_read_user_yes_no_default_yes(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr('click.prompt', lambda x, default, type: default)
    result = read_user_yes_no("Do you want to continue?", True)
    assert result is True

def test_read_user_yes_no_default_no(monkeypatch):
    runner = CliRunner()
    monkeypatch.setattr('click.prompt', lambda x, default, type: default)
    result = read_user_yes_no("Do you want to continue?", False)
    assert result is False
