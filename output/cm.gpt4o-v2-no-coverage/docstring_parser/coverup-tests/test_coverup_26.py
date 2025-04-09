# file: docstring_parser/numpydoc.py:117-154
# asked: {"lines": [136, 137, 145], "branches": [[131, 141], [133, 141], [135, 136], [142, 147], [144, 145]]}
# gained: {"lines": [136, 137, 145], "branches": [[133, 141], [135, 136], [144, 145]]}

import pytest
from docstring_parser.numpydoc import ParamSection
from docstring_parser.common import DocstringParam
import re

PARAM_KEY_REGEX = re.compile(r'(?P<name>\w+)(\s*:\s*(?P<type>[\w\s,]+))?')
PARAM_OPTIONAL_REGEX = re.compile(r'(?P<type>[\w\s,]+),\s*optional')
PARAM_DEFAULT_REGEX = re.compile(r'default\s*=\s*(?P<value>.+)')

def _clean_str(s: str) -> str:
    return s.strip()

class _KVSection:
    def __init__(self, title, key):
        self.title = title
        self.key = key

class TestParamSection:
    @pytest.fixture
    def param_section(self):
        return ParamSection("param", "param")

    def test_parse_item_with_type_and_optional(self, param_section):
        key = "arg_2 : int, optional"
        value = "description"
        result = param_section._parse_item(key, value)
        assert result.arg_name == "arg_2"
        assert result.type_name == "int"
        assert result.is_optional is True
        assert result.default is None
        assert result.description == "description"

    def test_parse_item_with_type_and_default(self, param_section):
        key = "arg_2 : int"
        value = "description default = 5"
        result = param_section._parse_item(key, value)
        assert result.arg_name == "arg_2"
        assert result.type_name == "int"
        assert result.is_optional is False
        assert result.default == "5"
        assert result.description == "description default = 5"

    def test_parse_item_without_type(self, param_section):
        key = "arg_2"
        value = "description"
        result = param_section._parse_item(key, value)
        assert result.arg_name == "arg_2"
        assert result.type_name is None
        assert result.is_optional is None
        assert result.default is None
        assert result.description == "description"

    def test_parse_item_with_multiline_description(self, param_section):
        key = "arg_2 : int, optional"
        value = "description can also span...\n... multiple lines"
        result = param_section._parse_item(key, value)
        assert result.arg_name == "arg_2"
        assert result.type_name == "int"
        assert result.is_optional is True
        assert result.default is None
        assert result.description == "description can also span...\n... multiple lines"
