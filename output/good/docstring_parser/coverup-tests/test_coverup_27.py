# file docstring_parser/rest.py:21-83
# lines [31]
# branches ['27->31']

import pytest
from docstring_parser.rest import _build_meta, DocstringParam, ParseError

PARAM_KEYWORDS = {"param", "parameter", "arg", "argument", "key", "keyword"}

@pytest.fixture
def mock_keywords(mocker):
    mocker.patch('docstring_parser.rest.PARAM_KEYWORDS', PARAM_KEYWORDS)

def test_build_meta_with_three_args_not_optional(mock_keywords):
    args = ["param", "int", "arg_name"]
    desc = "Description of the parameter."
    result = _build_meta(args, desc)
    assert isinstance(result, DocstringParam)
    assert result.args == args
    assert result.description == desc
    assert result.arg_name == "arg_name"
    assert result.type_name == "int"
    assert result.is_optional is False
    assert result.default is None
