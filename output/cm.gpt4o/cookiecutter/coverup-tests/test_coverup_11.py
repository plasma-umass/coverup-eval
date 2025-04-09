# file cookiecutter/prompt.py:99-119
# lines [99, 107, 108, 110, 112, 113, 116, 118, 119]
# branches ['107->108', '107->110', '116->118', '116->119']

import pytest
import click
from click.testing import CliRunner
from unittest.mock import patch
from cookiecutter.prompt import read_user_dict

def process_json(value):
    """Mock process_json function to simulate JSON processing."""
    return value

@pytest.fixture
def mock_click_prompt(mocker):
    return mocker.patch('click.prompt')

def test_read_user_dict_with_default_value(mock_click_prompt):
    mock_click_prompt.return_value = 'default'
    var_name = 'test_var'
    default_value = {'key': 'value'}
    
    result = read_user_dict(var_name, default_value)
    
    assert result == default_value

def test_read_user_dict_with_user_input(mock_click_prompt):
    user_input = '{"new_key": "new_value"}'
    mock_click_prompt.return_value = user_input
    var_name = 'test_var'
    default_value = {'key': 'value'}
    
    with patch('cookiecutter.prompt.process_json', side_effect=process_json):
        result = read_user_dict(var_name, default_value)
    
    assert result == user_input

def test_read_user_dict_with_invalid_default_value():
    var_name = 'test_var'
    default_value = 'not_a_dict'
    
    with pytest.raises(TypeError):
        read_user_dict(var_name, default_value)
