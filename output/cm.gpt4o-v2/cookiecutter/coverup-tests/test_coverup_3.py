# file: cookiecutter/prompt.py:99-119
# asked: {"lines": [99, 107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}
# gained: {"lines": [99, 107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch
from cookiecutter.prompt import read_user_dict

def process_json(value):
    # Dummy implementation for testing purposes
    return value

def test_read_user_dict_with_default_value():
    runner = CliRunner()
    default_value = {"key": "value"}

    with patch('click.prompt', return_value='default'):
        result = read_user_dict("Enter a dictionary", default_value)
        assert result == default_value

def test_read_user_dict_with_user_input():
    runner = CliRunner()
    default_value = {"key": "value"}
    user_input = '{"new_key": "new_value"}'

    with patch('click.prompt', return_value=user_input):
        result = read_user_dict("Enter a dictionary", default_value)
        assert result == user_input

def test_read_user_dict_with_non_dict_default():
    with pytest.raises(TypeError):
        read_user_dict("Enter a dictionary", "not_a_dict")
