# file: string_utils/manipulation.py:382-402
# asked: {"lines": [382, 397, 398, 400, 402], "branches": [[397, 398], [397, 400]]}
# gained: {"lines": [382, 397, 398, 400, 402], "branches": [[397, 398], [397, 400]]}

import pytest
from string_utils.manipulation import strip_html, InvalidInputError

def test_strip_html_remove_tags():
    input_string = 'test: <a href="foo/bar">click here</a>'
    expected_output = 'test: '
    assert strip_html(input_string) == expected_output

def test_strip_html_keep_tag_content():
    input_string = 'test: <a href="foo/bar">click here</a>'
    expected_output = 'test: click here'
    assert strip_html(input_string, keep_tag_content=True) == expected_output

def test_strip_html_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_html(12345)

def test_strip_html_empty_string():
    input_string = ''
    expected_output = ''
    assert strip_html(input_string) == expected_output

def test_strip_html_no_html():
    input_string = 'test: no html here'
    expected_output = 'test: no html here'
    assert strip_html(input_string) == expected_output
