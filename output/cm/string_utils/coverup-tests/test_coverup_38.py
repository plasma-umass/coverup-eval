# file string_utils/manipulation.py:382-402
# lines [382, 397, 398, 400, 402]
# branches ['397->398', '397->400']

import pytest
from string_utils.manipulation import strip_html

def test_strip_html_with_invalid_input():
    with pytest.raises(TypeError):
        strip_html(123)

def test_strip_html_without_keep_tag_content():
    result = strip_html('test: <a href="foo/bar">click here</a>')
    assert result == 'test: '

def test_strip_html_with_keep_tag_content():
    result = strip_html('test: <a href="foo/bar">click here</a>', keep_tag_content=True)
    assert result == 'test: click here'
