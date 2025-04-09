# file: cookiecutter/prompt.py:44-78
# asked: {"lines": [44, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 68, 69, 70, 71, 75, 76, 78], "branches": [[54, 55], [54, 57], [57, 58], [57, 60]]}
# gained: {"lines": [44, 54, 55, 57, 58, 60, 61, 63, 64, 66, 67, 68, 69, 70, 71, 75, 76, 78], "branches": [[54, 55], [54, 57], [57, 58], [57, 60]]}

import pytest
from collections import OrderedDict
import click
from click.testing import CliRunner
from cookiecutter.prompt import read_user_choice

def test_read_user_choice_valid(monkeypatch):
    options = ['option1', 'option2', 'option3']
    var_name = 'test_var'

    # Mock click.prompt to return '2'
    monkeypatch.setattr('click.prompt', lambda *args, **kwargs: '2')

    result = read_user_choice(var_name, options)
    assert result == 'option2'

def test_read_user_choice_invalid_type():
    with pytest.raises(TypeError):
        read_user_choice('test_var', 'not_a_list')

def test_read_user_choice_empty_list():
    with pytest.raises(ValueError):
        read_user_choice('test_var', [])

def test_read_user_choice_default(monkeypatch):
    options = ['option1', 'option2', 'option3']
    var_name = 'test_var'

    # Mock click.prompt to return the default value '1'
    monkeypatch.setattr('click.prompt', lambda *args, **kwargs: '1')

    result = read_user_choice(var_name, options)
    assert result == 'option1'

def test_read_user_choice_prompt(monkeypatch):
    options = ['option1', 'option2', 'option3']
    var_name = 'test_var'

    def mock_prompt(text, type, default, show_choices):
        assert 'Select test_var:' in text
        assert '1 - option1' in text
        assert '2 - option2' in text
        assert '3 - option3' in text
        assert 'Choose from 1, 2, 3' in text
        return '3'

    monkeypatch.setattr('click.prompt', mock_prompt)

    result = read_user_choice(var_name, options)
    assert result == 'option3'
