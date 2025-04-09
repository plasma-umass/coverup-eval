# file: cookiecutter/prompt.py:122-156
# asked: {"lines": [139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156], "branches": [[139, 140], [139, 141], [141, 142], [141, 148], [148, 149], [148, 150], [150, 151], [150, 153]]}
# gained: {"lines": [139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156], "branches": [[139, 140], [139, 141], [141, 142], [141, 148], [148, 149], [148, 150], [150, 151], [150, 153]]}

import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

@pytest.fixture
def jinja_env():
    return Environment()

def test_render_variable_none(jinja_env):
    assert render_variable(jinja_env, None, {}) is None

def test_render_variable_dict(jinja_env):
    raw = {"key": "value"}
    cookiecutter_dict = {}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == {"key": "value"}

def test_render_variable_list(jinja_env):
    raw = ["value1", "value2"]
    cookiecutter_dict = {}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == ["value1", "value2"]

def test_render_variable_non_str(jinja_env):
    raw = 123
    cookiecutter_dict = {}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == "123"

def test_render_variable_template(jinja_env):
    raw = "{{ cookiecutter.project_name.replace(' ', '_') }}"
    cookiecutter_dict = {"project_name": "Peanut Butter Cookie"}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == "Peanut_Butter_Cookie"
