# file cookiecutter/prompt.py:12-19
# lines [12, 19]
# branches []

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

# Assuming the function read_user_variable is imported from cookiecutter.prompt
from cookiecutter.prompt import read_user_variable

def test_read_user_variable(mocker):
    runner = CliRunner()

    # Mocking click.prompt to simulate user input
    mocker.patch('click.prompt', return_value='user_input_value')

    with runner.isolated_filesystem():
        result = read_user_variable('test_var', 'default_value')
        assert result == 'user_input_value'

    # Test with default value
    mocker.patch('click.prompt', return_value='default_value')
    with runner.isolated_filesystem():
        result = read_user_variable('test_var', 'default_value')
        assert result == 'default_value'
