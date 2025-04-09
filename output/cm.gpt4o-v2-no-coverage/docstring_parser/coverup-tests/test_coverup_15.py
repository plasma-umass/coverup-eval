# file: docstring_parser/google.py:89-114
# asked: {"lines": [89, 97, 99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 114], "branches": [[99, 103], [99, 106], [107, 108], [107, 114], [109, 110], [109, 112]]}
# gained: {"lines": [89, 97, 99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 114], "branches": [[99, 103], [99, 106], [107, 108], [109, 110], [109, 112]]}

import pytest
from unittest.mock import MagicMock
from docstring_parser.common import DocstringMeta
from enum import IntEnum

class SectionType(IntEnum):
    """Types of sections."""
    SINGULAR = 0
    'For sections like examples.'
    MULTIPLE = 1
    'For sections like params.'
    SINGULAR_OR_MULTIPLE = 2
    'For sections like returns or yields.'

@pytest.fixture
def parser():
    from docstring_parser.google import GoogleParser
    parser = GoogleParser()
    parser.sections = {
        'params': MagicMock(type=SectionType.SINGULAR, key='param'),
        'returns': MagicMock(type=SectionType.SINGULAR, key='return'),
        'raises': MagicMock(type=SectionType.SINGULAR, key='raise'),
        'yields': MagicMock(type=SectionType.SINGULAR, key='yield'),
        'multi': MagicMock(type=SectionType.SINGULAR_OR_MULTIPLE, key='param')
    }
    return parser

def test_build_meta_single(parser):
    parser._build_single_meta = MagicMock(return_value=DocstringMeta(args=['param'], description='description'))
    result = parser._build_meta('description', 'params')
    parser._build_single_meta.assert_called_once_with(parser.sections['params'], 'description')
    assert result.args == ['param']
    assert result.description == 'description'

def test_build_meta_multi(parser):
    parser._build_multi_meta = MagicMock(return_value=DocstringMeta(args=['param', 'before'], description='description'))
    result = parser._build_meta('before: description', 'multi')
    parser._build_multi_meta.assert_called_once_with(parser.sections['multi'], 'before', 'description')
    assert result.args == ['param', 'before']
    assert result.description == 'description'

def test_build_meta_multi_with_newline(parser):
    parser._build_multi_meta = MagicMock(return_value=DocstringMeta(args=['param', 'before'], description='first line\nrest of description'))
    result = parser._build_meta('before: first line\n    rest of description', 'multi')
    parser._build_multi_meta.assert_called_once_with(parser.sections['multi'], 'before', 'first line\nrest of description')
    assert result.args == ['param', 'before']
    assert result.description == 'first line\nrest of description'
