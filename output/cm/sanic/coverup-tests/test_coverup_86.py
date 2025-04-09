# file sanic/cookies.py:25-34
# lines [25, 31, 32, 34]
# branches ['31->32', '31->34']

import pytest
from sanic.cookies import _quote

# Assuming _Translator is a mapping table used by str.translate to quote special characters
# and _is_legal_key is a function that determines if a string is a legal cookie key.
# Since these are not provided in the snippet, we will mock them for the purpose of the test.

@pytest.fixture
def mock_translator(mocker):
    translator = {ord(';'): '\\073', ord(','): '\\054'}
    return translator

@pytest.fixture
def mock_is_legal_key(mocker):
    return mocker.patch('sanic.cookies._is_legal_key', return_value=False)

def test_quote_with_illegal_key_needing_quotes(mock_translator, mock_is_legal_key):
    illegal_str = 'some;illegal,key'
    expected_quoted_str = '"' + illegal_str.translate(mock_translator) + '"'
    assert _quote(illegal_str) == expected_quoted_str
    mock_is_legal_key.assert_called_once_with(illegal_str)

def test_quote_with_none():
    assert _quote(None) is None

def test_quote_with_legal_key(mocker):
    legal_str = 'legal_key'
    mocker.patch('sanic.cookies._is_legal_key', return_value=True)
    assert _quote(legal_str) == legal_str
