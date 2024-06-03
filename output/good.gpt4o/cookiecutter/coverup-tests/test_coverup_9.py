# file cookiecutter/prompt.py:122-156
# lines [122, 139, 140, 141, 142, 143, 144, 146, 148, 149, 150, 151, 153, 155, 156]
# branches ['139->140', '139->141', '141->142', '141->148', '148->149', '148->150', '150->151', '150->153']

import pytest
from jinja2 import Environment
from cookiecutter.prompt import render_variable

def test_render_variable_none():
    env = Environment()
    result = render_variable(env, None, {})
    assert result is None

def test_render_variable_dict():
    env = Environment()
    raw = {"key1": "{{ cookiecutter.value1 }}", "key2": "{{ cookiecutter.value2 }}"}
    cookiecutter_dict = {"value1": "val1", "value2": "val2"}
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == {"key1": "val1", "key2": "val2"}

def test_render_variable_list():
    env = Environment()
    raw = ["{{ cookiecutter.value1 }}", "{{ cookiecutter.value2 }}"]
    cookiecutter_dict = {"value1": "val1", "value2": "val2"}
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == ["val1", "val2"]

def test_render_variable_non_str():
    env = Environment()
    raw = 123
    cookiecutter_dict = {}
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == "123"

def test_render_variable_str():
    env = Environment()
    raw = "{{ cookiecutter.value }}"
    cookiecutter_dict = {"value": "val"}
    result = render_variable(env, raw, cookiecutter_dict)
    assert result == "val"
