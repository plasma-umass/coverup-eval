# file docstring_parser/numpydoc.py:117-154
# lines [117, 118, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153]
# branches ['131->132', '131->141', '133->134', '133->141', '135->136', '135->139', '142->143', '142->147', '144->145', '144->147']

import re
import pytest
from docstring_parser.numpydoc import ParamSection, DocstringParam

# Assuming the regex patterns are defined somewhere in the module as follows:
PARAM_KEY_REGEX = re.compile(r'(?P<name>\w+)(?:\s*:\s*(?P<type>[\w\[\],\s]+))?')
PARAM_OPTIONAL_REGEX = re.compile(r'(?P<type>[\w\[\]]+)(?:,\s*optional)?')
PARAM_DEFAULT_REGEX = re.compile(r'\[default:\s*(?P<value>.+?)\]')

# Mock _clean_str function
def _clean_str(s):
    return s.strip()

# Test function to improve coverage
def test_param_section_parse_item():
    param_section = ParamSection('Parameters', 'param')

    # Case where type is optional
    key = "param_1 : int, optional"
    value = "The first parameter [default: 10]"
    result = param_section._parse_item(key, value)
    assert result.arg_name == "param_1"
    assert result.type_name == "int"
    assert result.is_optional is True
    assert result.default == "10"

    # Case where type is not optional
    key = "param_2 : str"
    value = "The second parameter"
    result = param_section._parse_item(key, value)
    assert result.arg_name == "param_2"
    assert result.type_name == "str"
    assert result.is_optional is False
    assert result.default is None

    # Case where there is no type and no default
    key = "param_3"
    value = "The third parameter"
    result = param_section._parse_item(key, value)
    assert result.arg_name == "param_3"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.default is None

    # Case where there is a default but no type
    key = "param_4"
    value = "The fourth parameter [default: None]"
    result = param_section._parse_item(key, value)
    assert result.arg_name == "param_4"
    assert result.type_name is None
    assert result.is_optional is None
    assert result.default == "None"
