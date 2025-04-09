# file: cookiecutter/prompt.py:44-78
# asked: {"lines": [44, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 68, 69, 70, 71, 75, 76, 78], "branches": [[54, 55], [54, 57], [57, 58], [57, 60]]}
# gained: {"lines": [44, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 68, 69, 70, 71, 75, 76, 78], "branches": [[54, 55], [54, 57], [57, 58], [57, 60]]}

import pytest
from collections import OrderedDict
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_choice

def test_read_user_choice_invalid_options_type():
    with pytest.raises(TypeError):
        read_user_choice("variable", "not_a_list")

def test_read_user_choice_empty_options():
    with pytest.raises(ValueError):
        read_user_choice("variable", [])

def test_read_user_choice_valid_options(monkeypatch):
    options = ["option1", "option2", "option3"]
    var_name = "variable"
    
    # Mock click.prompt to return a specific choice
    monkeypatch.setattr('click.prompt', lambda *args, **kwargs: '2')
    
    result = read_user_choice(var_name, options)
    
    assert result == "option2"

def test_read_user_choice_default(monkeypatch):
    options = ["option1", "option2", "option3"]
    var_name = "variable"
    
    # Mock click.prompt to return the default choice
    monkeypatch.setattr('click.prompt', lambda *args, **kwargs: '1')
    
    result = read_user_choice(var_name, options)
    
    assert result == "option1"
