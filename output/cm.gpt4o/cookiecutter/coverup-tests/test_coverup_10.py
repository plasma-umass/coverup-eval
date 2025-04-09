# file cookiecutter/prompt.py:22-32
# lines [22, 32]
# branches []

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

# Assuming the function read_user_yes_no is imported from cookiecutter.prompt
from cookiecutter.prompt import read_user_yes_no

def test_read_user_yes_no_yes(mocker):
    runner = CliRunner()
    question = "Do you want to continue?"
    default_value = True

    with runner.isolated_filesystem():
        mocker.patch('click.prompt', return_value=True)
        result = read_user_yes_no(question, default_value)
        assert result is True

def test_read_user_yes_no_no(mocker):
    runner = CliRunner()
    question = "Do you want to continue?"
    default_value = False

    with runner.isolated_filesystem():
        mocker.patch('click.prompt', return_value=False)
        result = read_user_yes_no(question, default_value)
        assert result is False

def test_read_user_yes_no_default(mocker):
    runner = CliRunner()
    question = "Do you want to continue?"
    default_value = True

    with runner.isolated_filesystem():
        mocker.patch('click.prompt', return_value=default_value)
        result = read_user_yes_no(question, default_value)
        assert result is True

def test_read_user_yes_no_invalid_input(mocker):
    runner = CliRunner()
    question = "Do you want to continue?"
    default_value = True

    with runner.isolated_filesystem():
        mocker.patch('click.prompt', side_effect=click.exceptions.BadParameter("Invalid input"))
        with pytest.raises(click.exceptions.BadParameter):
            read_user_yes_no(question, default_value)
