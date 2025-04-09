# file: cookiecutter/prompt.py:22-32
# asked: {"lines": [32], "branches": []}
# gained: {"lines": [32], "branches": []}

import pytest
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_yes_no

def test_read_user_yes_no_default_yes(monkeypatch):
    runner = CliRunner()

    def mock_prompt(*args, **kwargs):
        return True

    monkeypatch.setattr(click, 'prompt', mock_prompt)
    result = read_user_yes_no("Do you want to continue?", True)
    assert result is True

def test_read_user_yes_no_default_no(monkeypatch):
    runner = CliRunner()

    def mock_prompt(*args, **kwargs):
        return False

    monkeypatch.setattr(click, 'prompt', mock_prompt)
    result = read_user_yes_no("Do you want to continue?", False)
    assert result is False

def test_read_user_yes_no_user_input_yes(monkeypatch):
    runner = CliRunner()

    def mock_prompt(*args, **kwargs):
        return True

    monkeypatch.setattr(click, 'prompt', mock_prompt)
    result = read_user_yes_no("Do you want to continue?", None)
    assert result is True

def test_read_user_yes_no_user_input_no(monkeypatch):
    runner = CliRunner()

    def mock_prompt(*args, **kwargs):
        return False

    monkeypatch.setattr(click, 'prompt', mock_prompt)
    result = read_user_yes_no("Do you want to continue?", None)
    assert result is False
