# file: cookiecutter/prompt.py:99-119
# asked: {"lines": [107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}
# gained: {"lines": [107, 108, 110, 112, 113, 116, 118, 119], "branches": [[107, 108], [107, 110], [116, 118], [116, 119]]}

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch
from cookiecutter.prompt import read_user_dict

def process_json(value):
    # Dummy implementation for process_json
    return value

def test_read_user_dict_with_non_dict_default():
    with pytest.raises(TypeError):
        read_user_dict("Enter data", "not a dict")

def test_read_user_dict_with_default_value(monkeypatch):
    default_value = {"key": "value"}
    
    def mock_prompt(*args, **kwargs):
        return 'default'
    
    monkeypatch.setattr(click, 'prompt', mock_prompt)
    
    result = read_user_dict("Enter data", default_value)
    assert result == default_value

def test_read_user_dict_with_user_input(monkeypatch):
    default_value = {"key": "value"}
    user_input = '{"new_key": "new_value"}'
    
    def mock_prompt(*args, **kwargs):
        return user_input
    
    monkeypatch.setattr(click, 'prompt', mock_prompt)
    
    result = read_user_dict("Enter data", default_value)
    assert result == user_input
