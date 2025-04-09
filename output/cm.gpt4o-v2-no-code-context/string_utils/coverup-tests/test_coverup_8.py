# file: string_utils/validation.py:532-552
# asked: {"lines": [532, 547, 548, 550, 552], "branches": [[547, 548], [547, 550]]}
# gained: {"lines": [532, 547, 548, 550, 552], "branches": [[547, 548], [547, 550]]}

import pytest
from string_utils.validation import is_slug

def test_is_slug_valid_slug():
    assert is_slug('my-blog-post-title') is True

def test_is_slug_invalid_slug():
    assert is_slug('My blog post title') is False

def test_is_slug_empty_string():
    assert is_slug('') is False

def test_is_slug_non_string_input():
    assert is_slug(12345) is False

def test_is_slug_custom_separator():
    assert is_slug('my_blog_post_title', separator='_') is True

def test_is_slug_invalid_custom_separator():
    assert is_slug('my-blog-post-title', separator='_') is False
