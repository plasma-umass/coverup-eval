# file: docstring_parser/numpydoc.py:117-154
# asked: {"lines": [117, 118, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153], "branches": [[131, 132], [131, 141], [133, 134], [133, 141], [135, 136], [135, 139], [142, 143], [142, 147], [144, 145], [144, 147]]}
# gained: {"lines": [117, 118, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153], "branches": [[131, 132], [133, 134], [133, 141], [135, 136], [135, 139], [142, 143], [144, 145], [144, 147]]}

import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam

@pytest.fixture
def param_section():
    return ParamSection(title="Parameters", key="param")

def test_parse_item_with_type_and_optional(param_section):
    key = "arg_2 : type, optional"
    value = "descriptions can also span...\n... multiple lines"
    result = param_section._parse_item(key, value)
    
    assert result.arg_name == "arg_2"
    assert result.type_name == "type"
    assert result.is_optional is True
    assert result.description == value.strip()
    assert result.default is None

def test_parse_item_with_type_and_not_optional(param_section):
    key = "arg_2 : type"
    value = "descriptions can also span...\n... multiple lines"
    result = param_section._parse_item(key, value)
    
    assert result.arg_name == "arg_2"
    assert result.type_name == "type"
    assert result.is_optional is False
    assert result.description == value.strip()
    assert result.default is None

def test_parse_item_without_type(param_section):
    key = "arg_name"
    value = "arg_description"
    result = param_section._parse_item(key, value)
    
    assert result.arg_name == "arg_name"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.description == value.strip()
    assert result.default is None

def test_parse_item_with_default(param_section):
    key = "arg_2 : type, optional"
    value = "descriptions can also span...\n... multiple lines\nDefault: 42"
    result = param_section._parse_item(key, value)
    
    assert result.arg_name == "arg_2"
    assert result.type_name == "type"
    assert result.is_optional is True
    assert result.description == value.strip()
    assert result.default == "42"
