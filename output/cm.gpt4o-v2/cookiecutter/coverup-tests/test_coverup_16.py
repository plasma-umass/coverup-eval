# file: cookiecutter/prompt.py:171-229
# asked: {"lines": [177, 178, 183, 184, 185, 186, 187, 188, 189, 191, 192, 194, 195, 197, 198, 200, 202, 203, 205, 206, 207, 208, 211, 213, 214, 216, 217, 219, 221, 222, 224, 225, 226, 227, 229], "branches": [[183, 184], [183, 211], [184, 185], [184, 187], [187, 188], [187, 191], [192, 194], [192, 198], [198, 183], [198, 200], [202, 203], [202, 205], [211, 213], [211, 229], [213, 214], [213, 216], [217, 211], [217, 219], [221, 222], [221, 224]]}
# gained: {"lines": [177, 178, 183, 184, 185, 186, 187, 188, 189, 191, 192, 194, 195, 197, 198, 200, 202, 203, 205, 206, 207, 208, 211, 213, 214, 216, 217, 219, 221, 222, 224, 229], "branches": [[183, 184], [183, 211], [184, 185], [184, 187], [187, 188], [187, 191], [192, 194], [192, 198], [198, 183], [198, 200], [202, 203], [202, 205], [211, 213], [211, 229], [213, 214], [213, 216], [217, 211], [217, 219], [221, 222], [221, 224]]}

import pytest
from collections import OrderedDict
from jinja2.exceptions import UndefinedError
from cookiecutter.environment import StrictEnvironment
from cookiecutter.exceptions import UndefinedVariableInTemplate, UnknownExtension
from cookiecutter.prompt import prompt_for_config
from cookiecutter.prompt import render_variable, prompt_choice_for_config, read_user_variable, read_user_dict

@pytest.fixture
def mock_env(mocker):
    mocker.patch('cookiecutter.environment.StrictEnvironment.__init__', return_value=None)
    return StrictEnvironment()

@pytest.fixture
def mock_prompt_choice_for_config(mocker):
    return mocker.patch('cookiecutter.prompt.prompt_choice_for_config')

@pytest.fixture
def mock_render_variable(mocker):
    return mocker.patch('cookiecutter.prompt.render_variable')

@pytest.fixture
def mock_read_user_variable(mocker):
    return mocker.patch('cookiecutter.prompt.read_user_variable')

@pytest.fixture
def mock_read_user_dict(mocker):
    return mocker.patch('cookiecutter.prompt.read_user_dict')

def test_prompt_for_config_no_input(mock_env, mock_render_variable, mock_prompt_choice_for_config, mock_read_user_variable, mock_read_user_dict):
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            '_private_var': 'private',
            '__public_var': 'public',
            'choice_var': ['option1', 'option2'],
            'regular_var': 'value',
            'dict_var': {'key': 'value'}
        }
    }
    mock_render_variable.side_effect = lambda env, raw, cookiecutter_dict: raw
    mock_prompt_choice_for_config.side_effect = lambda cookiecutter_dict, env, key, raw, no_input: raw[0]
    mock_read_user_variable.side_effect = lambda key, val: val
    mock_read_user_dict.side_effect = lambda key, val: val

    result = prompt_for_config(context, no_input=True)

    assert result == {
        'project_name': 'Test Project',
        '_private_var': 'private',
        '__public_var': 'public',
        'choice_var': 'option1',
        'regular_var': 'value',
        'dict_var': {'key': 'value'}
    }

def test_prompt_for_config_with_input(mock_env, mock_render_variable, mock_prompt_choice_for_config, mock_read_user_variable, mock_read_user_dict):
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            '_private_var': 'private',
            '__public_var': 'public',
            'choice_var': ['option1', 'option2'],
            'regular_var': 'value',
            'dict_var': {'key': 'value'}
        }
    }
    mock_render_variable.side_effect = lambda env, raw, cookiecutter_dict: raw
    mock_prompt_choice_for_config.side_effect = lambda cookiecutter_dict, env, key, raw, no_input: raw[0]
    mock_read_user_variable.side_effect = lambda key, val: val
    mock_read_user_dict.side_effect = lambda key, val: val

    result = prompt_for_config(context, no_input=False)

    assert result == {
        'project_name': 'Test Project',
        '_private_var': 'private',
        '__public_var': 'public',
        'choice_var': 'option1',
        'regular_var': 'value',
        'dict_var': {'key': 'value'}
    }

def test_prompt_for_config_undefined_error(mock_env, mock_render_variable):
    context = {
        'cookiecutter': {
            'project_name': 'Test Project',
            'undefined_var': '{{ cookiecutter.undefined }}'
        }
    }
    mock_render_variable.side_effect = UndefinedError

    with pytest.raises(UndefinedVariableInTemplate):
        prompt_for_config(context, no_input=True)
