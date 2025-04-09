# file cookiecutter/prompt.py:122-156
# lines [122, 139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156]
# branches ['139->140', '139->141', '141->142', '141->148', '148->149', '148->150', '150->151', '150->153']

import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

@pytest.fixture
def env():
    return Environment()

@pytest.fixture
def cookiecutter_dict():
    return {'project_name': 'Peanut Butter Cookie'}

def test_render_variable_with_dict(env, cookiecutter_dict):
    raw = {
        'repo_name': '{{ cookiecutter.project_name.replace(" ", "_") }}',
        'author_name': 'Oreo Milkshake'
    }
    expected = {
        'repo_name': 'Peanut_Butter_Cookie',
        'author_name': 'Oreo Milkshake'
    }
    assert render_variable(env, raw, cookiecutter_dict) == expected

def test_render_variable_with_list(env, cookiecutter_dict):
    raw = ['{{ cookiecutter.project_name.upper() }}', 'Chocolate_Chip']
    expected = ['PEANUT BUTTER COOKIE', 'Chocolate_Chip']
    assert render_variable(env, raw, cookiecutter_dict) == expected

def test_render_variable_with_non_string(env, cookiecutter_dict):
    raw = 12345
    expected = '12345'
    assert render_variable(env, raw, cookiecutter_dict) == expected

def test_render_variable_with_none(env, cookiecutter_dict):
    raw = None
    expected = None
    assert render_variable(env, raw, cookiecutter_dict) == expected
