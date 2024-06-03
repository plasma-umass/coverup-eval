# file sanic/cookies.py:25-34
# lines [25, 31, 32, 34]
# branches ['31->32', '31->34']

import pytest
from sanic.cookies import _quote

def test_quote_none():
    assert _quote(None) is None

def test_quote_legal_key(mocker):
    mocker.patch('sanic.cookies._is_legal_key', return_value=True)
    assert _quote("legal_key") == "legal_key"

def test_quote_illegal_key(mocker):
    mocker.patch('sanic.cookies._is_legal_key', return_value=False)
    mocker.patch('sanic.cookies._Translator', str.maketrans({
        '"': r'\"',
        '\\': r'\\',
        '\t': r'\t',
        '\r': r'\r',
        '\n': r'\n',
        '\x0b': r'\x0b',
        '\x0c': r'\x0c',
    }))
    assert _quote("illegal_key") == '"illegal_key"'
    assert _quote("a") == '"a"'
    assert _quote('a"b') == r'"a\"b"'
    assert _quote('a\\b') == r'"a\\b"'
    assert _quote('a\tb') == r'"a\tb"'
    assert _quote('a\rb') == r'"a\rb"'
    assert _quote('a\nb') == r'"a\nb"'
    assert _quote('a\x0bb') == r'"a\x0bb"'
    assert _quote('a\x0cb') == r'"a\x0cb"'
