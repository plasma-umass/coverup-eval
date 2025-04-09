# file: cookiecutter/prompt.py:99-119
# asked: {"lines": [99, 107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}
# gained: {"lines": [99, 107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch
from cookiecutter.prompt import read_user_dict, process_json

def test_read_user_dict_with_default_value():
    var_name = "test_var"
    default_value = {"key": "value"}

    runner = CliRunner()
    with patch('click.prompt', return_value='default'):
        result = read_user_dict(var_name, default_value)
        assert result == default_value

def test_read_user_dict_with_user_input():
    var_name = "test_var"
    default_value = {"key": "value"}
    user_input = {"new_key": "new_value"}

    runner = CliRunner()
    with patch('click.prompt', return_value=user_input):
        result = read_user_dict(var_name, default_value)
        assert result == user_input

def test_read_user_dict_raises_type_error():
    var_name = "test_var"
    default_value = "not_a_dict"

    with pytest.raises(TypeError):
        read_user_dict(var_name, default_value)

def test_process_json_valid_input():
    user_input = '{"key": "value"}'
    result = process_json(user_input)
    assert result == {"key": "value"}

def test_process_json_invalid_json():
    user_input = 'invalid_json'

    with pytest.raises(click.UsageError, match='Unable to decode to JSON.'):
        process_json(user_input)

def test_process_json_not_a_dict():
    user_input = '["not", "a", "dict"]'

    with pytest.raises(click.UsageError, match='Requires JSON dict.'):
        process_json(user_input)
