# file: cookiecutter/prompt.py:122-156
# asked: {"lines": [122, 139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156], "branches": [[139, 140], [139, 141], [141, 142], [141, 148], [148, 149], [148, 150], [150, 151], [150, 153]]}
# gained: {"lines": [122, 139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156], "branches": [[139, 140], [139, 141], [141, 142], [141, 148], [148, 149], [148, 150], [150, 151], [150, 153]]}

import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

@pytest.fixture
def jinja_env():
    return Environment()

def test_render_variable_none(jinja_env):
    result = render_variable(jinja_env, None, {})
    assert result is None

def test_render_variable_dict(jinja_env):
    raw = {"key1": "{{ cookiecutter.project_name }}_suffix", "key2": "static_value"}
    cookiecutter_dict = {"project_name": "TestProject"}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == {"key1": "TestProject_suffix", "key2": "static_value"}

def test_render_variable_list(jinja_env):
    raw = ["{{ cookiecutter.project_name }}_suffix", "static_value"]
    cookiecutter_dict = {"project_name": "TestProject"}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == ["TestProject_suffix", "static_value"]

def test_render_variable_non_str(jinja_env):
    raw = 12345
    cookiecutter_dict = {"project_name": "TestProject"}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == "12345"

def test_render_variable_str(jinja_env):
    raw = "{{ cookiecutter.project_name }}_suffix"
    cookiecutter_dict = {"project_name": "TestProject"}
    result = render_variable(jinja_env, raw, cookiecutter_dict)
    assert result == "TestProject_suffix"
