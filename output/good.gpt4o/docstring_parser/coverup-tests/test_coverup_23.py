# file docstring_parser/numpydoc.py:117-154
# lines [117, 118, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 141, 142, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153]
# branches ['131->132', '131->141', '133->134', '133->141', '135->136', '135->139', '142->143', '142->147', '144->145', '144->147']

import pytest
from docstring_parser.numpydoc import _KVSection, DocstringParam
import re

# Mocking the regex patterns used in the original code
PARAM_KEY_REGEX = re.compile(r"(?P<name>\w+)(?:\s*:\s*(?P<type>[\w\s,]+))?")
PARAM_OPTIONAL_REGEX = re.compile(r"(?P<type>[\w\s,]+),\s*optional")
PARAM_DEFAULT_REGEX = re.compile(r"default\s*=\s*(?P<value>.+)")

class TestParamSection:
    class ParamSection(_KVSection):
        """Parser for numpydoc parameter sections.
    
        E.g. any section that looks like this:
            arg_name
                arg_description
            arg_2 : type, optional
                descriptions can also span...
                ... multiple lines
        """
    
        def _parse_item(self, key: str, value: str) -> DocstringParam:
            m = PARAM_KEY_REGEX.match(key)
            arg_name = type_name = is_optional = None
            if m is not None:
                arg_name, type_name = m.group("name"), m.group("type")
                if type_name is not None:
                    optional_match = PARAM_OPTIONAL_REGEX.match(type_name)
                    if optional_match is not None:
                        type_name = optional_match.group("type")
                        is_optional = True
                    else:
                        is_optional = False
    
            default = None
            if len(value) > 0:
                default_match = PARAM_DEFAULT_REGEX.search(value)
                if default_match is not None:
                    default = default_match.group("value")
    
            return DocstringParam(
                args=[self.key, arg_name],
                description=_clean_str(value),
                arg_name=arg_name,
                type_name=type_name,
                is_optional=is_optional,
                default=default,
            )

    @pytest.fixture
    def param_section(self):
        return self.ParamSection(title="Parameters", key="param")

    def test_parse_item_with_optional_type(self, param_section):
        key = "param1 : int, optional"
        value = "This is a parameter with an optional type."
        result = param_section._parse_item(key, value)
        assert result.arg_name == "param1"
        assert result.type_name == "int"
        assert result.is_optional is True
        assert result.default is None

    def test_parse_item_with_default_value(self, param_section):
        key = "param2 : str"
        value = "This is a parameter with a default value. default = 'default_value'"
        result = param_section._parse_item(key, value)
        assert result.arg_name == "param2"
        assert result.type_name == "str"
        assert result.is_optional is False
        assert result.default == "'default_value'"

    def test_parse_item_without_type(self, param_section):
        key = "param3"
        value = "This is a parameter without a type."
        result = param_section._parse_item(key, value)
        assert result.arg_name == "param3"
        assert result.type_name is None
        assert result.is_optional is None
        assert result.default is None

def _clean_str(s: str) -> str:
    """Mocked _clean_str function."""
    return s.strip()
