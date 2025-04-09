# file: string_utils/validation.py:532-552
# asked: {"lines": [532, 547, 548, 550, 552], "branches": [[547, 548], [547, 550]]}
# gained: {"lines": [532, 547, 548, 550, 552], "branches": [[547, 548], [547, 550]]}

import pytest
from string_utils.validation import is_slug

def test_is_slug_valid_slug():
    assert is_slug('my-blog-post-title') == True

def test_is_slug_invalid_slug():
    assert is_slug('My blog post title') == False

def test_is_slug_empty_string():
    assert is_slug('') == False

def test_is_slug_none():
    assert is_slug(None) == False

def test_is_slug_custom_separator():
    assert is_slug('my_blog_post_title', '_') == True

def test_is_slug_invalid_custom_separator():
    assert is_slug('my-blog-post-title', '_') == False

def test_is_slug_trailing_separator():
    assert is_slug('my-blog-post-title-', '-') == False

def test_is_slug_leading_separator():
    assert is_slug('-my-blog-post-title', '-') == False

def test_is_slug_multiple_separators():
    assert is_slug('my--blog--post--title', '-') == True

def test_is_slug_special_characters():
    assert is_slug('my-blog-post-title!', '-') == False
