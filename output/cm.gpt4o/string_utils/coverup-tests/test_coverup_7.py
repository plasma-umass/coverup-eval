# file string_utils/validation.py:532-552
# lines [532, 547, 548, 550, 552]
# branches ['547->548', '547->550']

import pytest
from string_utils.validation import is_slug

def test_is_slug_valid_slug():
    assert is_slug('my-blog-post-title') == True

def test_is_slug_invalid_slug():
    assert is_slug('My blog post title') == False

def test_is_slug_empty_string():
    assert is_slug('') == False

def test_is_slug_with_different_separator():
    assert is_slug('my_blog_post_title', separator='_') == True

def test_is_slug_with_invalid_separator():
    assert is_slug('my-blog-post-title', separator='_') == False

def test_is_slug_non_string_input():
    assert is_slug(12345) == False
    assert is_slug(None) == False
    assert is_slug(['my', 'blog', 'post', 'title']) == False
