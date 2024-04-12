# file string_utils/validation.py:532-552
# lines [532, 547, 548, 550, 552]
# branches ['547->548', '547->550']

import pytest
from string_utils.validation import is_slug

def test_is_slug_with_non_string_input():
    assert not is_slug(None), "None should not be considered a slug"
    assert not is_slug(123), "Integer should not be considered a slug"
    assert not is_slug([]), "List should not be considered a slug"
    assert not is_slug({}), "Dictionary should not be considered a slug"

def test_is_slug_with_various_separators():
    assert is_slug('my-blog-post-title'), "Valid slug with default separator"
    assert not is_slug('my_blog_post_title'), "Invalid slug with default separator"
    assert is_slug('my_blog_post_title', separator='_'), "Valid slug with custom separator"
    assert not is_slug('my*blog*post*title', separator='_'), "Invalid slug with custom separator"
    assert is_slug('my*blog*post*title', separator='*'), "Valid slug with custom separator"
    assert not is_slug('my blog post title', separator='-'), "Invalid slug with spaces"

def test_is_slug_with_edge_cases():
    assert not is_slug(''), "Empty string should not be considered a slug"
    assert not is_slug('-'), "Single separator should not be considered a slug"
    assert not is_slug('---'), "Multiple separators should not be considered a slug"
    assert is_slug('a-b'), "Valid slug with single characters"
    assert is_slug('a--b'), "Valid slug with consecutive separators"
    assert is_slug('a'), "Single character should be considered a slug"
    assert not is_slug('a-'), "Slug should not end with a separator"
    assert not is_slug('-a'), "Slug should not start with a separator"
