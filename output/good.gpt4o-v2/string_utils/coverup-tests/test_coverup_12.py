# file: string_utils/manipulation.py:382-402
# asked: {"lines": [382, 397, 398, 400, 402], "branches": [[397, 398], [397, 400]]}
# gained: {"lines": [382, 397, 398, 400, 402], "branches": [[397, 398], [397, 400]]}

import pytest
from string_utils.manipulation import strip_html
from string_utils.errors import InvalidInputError

def test_strip_html_removes_html():
    assert strip_html('test: <a href="foo/bar">click here</a>') == 'test: '

def test_strip_html_keeps_tag_content():
    assert strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True) == 'test: click here'

def test_strip_html_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_html(123)

def test_strip_html_empty_string():
    assert strip_html('') == ''

def test_strip_html_no_html():
    assert strip_html('no html here') == 'no html here'
