# file: cookiecutter/prompt.py:99-119
# asked: {"lines": [107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}
# gained: {"lines": [107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch

# Assuming the function read_user_dict is imported from cookiecutter.prompt
from cookiecutter.prompt import read_user_dict

def process_json(value):
    # Dummy implementation of process_json for testing purposes
    return value

def test_read_user_dict_with_non_dict_default():
    with pytest.raises(TypeError):
        read_user_dict("test_var", "not_a_dict")

def test_read_user_dict_with_default_display(monkeypatch):
    runner = CliRunner()

    def mock_prompt(*args, **kwargs):
        return 'default'

    monkeypatch.setattr(click, 'prompt', mock_prompt)

    result = read_user_dict("test_var", {"key": "value"})
    assert result == {"key": "value"}

def test_read_user_dict_with_user_input(monkeypatch):
    runner = CliRunner()

    def mock_prompt(*args, **kwargs):
        return '{"new_key": "new_value"}'

    monkeypatch.setattr(click, 'prompt', mock_prompt)

    result = read_user_dict("test_var", {"key": "value"})
    assert result == '{"new_key": "new_value"}'
