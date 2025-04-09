# file: string_utils/manipulation.py:462-497
# asked: {"lines": [462, 485, 486, 489, 492, 495, 497], "branches": [[485, 486], [485, 489]]}
# gained: {"lines": [462, 485, 486, 489, 492, 495, 497], "branches": [[485, 486], [485, 489]]}

import pytest
from string_utils.manipulation import slugify, InvalidInputError
import re

def test_slugify_valid_string():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Hello, World!') == 'hello-world'
    assert slugify('Python@3.9') == 'python-3-9'

def test_slugify_custom_separator():
    assert slugify('Top 10 Reasons To Love Dogs!!!', '_') == 'top_10_reasons_to_love_dogs'
    assert slugify('Mönstér Mägnët', '_') == 'monster_magnet'
    assert slugify('Hello, World!', '_') == 'hello_world'
    assert slugify('Python@3.9', '_') == 'python_3_9'

def test_slugify_invalid_input():
    with pytest.raises(InvalidInputError):
        slugify(12345)
    with pytest.raises(InvalidInputError):
        slugify(None)
    with pytest.raises(InvalidInputError):
        slugify(['list', 'of', 'strings'])

def test_slugify_edge_cases():
    assert slugify('') == ''
    assert slugify('     ') == ''
    assert slugify('---') == ''
    assert slugify('___', '_') == ''
    assert slugify('!!!') == ''
    assert slugify('a' * 1000) == 'a' * 1000

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up any state if necessary
    yield
    # No specific cleanup needed for this test
