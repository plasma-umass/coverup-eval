# file: cookiecutter/prompt.py:122-156
# asked: {"lines": [122, 139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156], "branches": [[139, 140], [139, 141], [141, 142], [141, 148], [148, 149], [148, 150], [150, 151], [150, 153]]}
# gained: {"lines": [122, 139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156], "branches": [[139, 140], [139, 141], [141, 142], [141, 148], [148, 149], [148, 150], [150, 151], [150, 153]]}

import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

@pytest.fixture
def env():
    return Environment()

def test_render_variable_none(env):
    assert render_variable(env, None, {}) is None

def test_render_variable_dict(env):
    raw = {"key1": "{{ cookiecutter.project_name }}", "key2": "value2"}
    cookiecutter_dict = {"project_name": "TestProject"}
    expected = {"key1": "TestProject", "key2": "value2"}
    assert render_variable(env, raw, cookiecutter_dict) == expected

def test_render_variable_list(env):
    raw = ["{{ cookiecutter.project_name }}", "value2"]
    cookiecutter_dict = {"project_name": "TestProject"}
    expected = ["TestProject", "value2"]
    assert render_variable(env, raw, cookiecutter_dict) == expected

def test_render_variable_non_str(env):
    raw = 123
    cookiecutter_dict = {}
    expected = "123"
    assert render_variable(env, raw, cookiecutter_dict) == expected

def test_render_variable_str(env):
    raw = "{{ cookiecutter.project_name }}"
    cookiecutter_dict = {"project_name": "TestProject"}
    expected = "TestProject"
    assert render_variable(env, raw, cookiecutter_dict) == expected
