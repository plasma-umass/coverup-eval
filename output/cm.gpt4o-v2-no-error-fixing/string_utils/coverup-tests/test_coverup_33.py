# file: string_utils/manipulation.py:462-497
# asked: {"lines": [462, 485, 486, 489, 492, 495, 497], "branches": [[485, 486], [485, 489]]}
# gained: {"lines": [462, 485, 486, 489, 492, 495, 497], "branches": [[485, 486], [485, 489]]}

import pytest
from string_utils.manipulation import slugify
from string_utils.errors import InvalidInputError

def test_slugify_valid_string():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Hello, World!') == 'hello-world'
    assert slugify('Python_is_awesome') == 'python-is-awesome'
    assert slugify('  Leading and trailing spaces  ') == 'leading-and-trailing-spaces'

def test_slugify_custom_separator():
    assert slugify('Top 10 Reasons To Love Dogs!!!', '_') == 'top_10_reasons_to_love_dogs'
    assert slugify('Mönstér Mägnët', '_') == 'monster_magnet'
    assert slugify('Hello, World!', '_') == 'hello_world'
    assert slugify('Python_is_awesome', '_') == 'python_is_awesome'
    assert slugify('  Leading and trailing spaces  ', '_') == 'leading_and_trailing_spaces'

def test_slugify_invalid_input():
    with pytest.raises(InvalidInputError):
        slugify(12345)
    with pytest.raises(InvalidInputError):
        slugify(None)
    with pytest.raises(InvalidInputError):
        slugify(['list', 'of', 'strings'])
    with pytest.raises(InvalidInputError):
        slugify({'key': 'value'})

def test_slugify_edge_cases():
    assert slugify('') == ''
    assert slugify('     ') == ''
    assert slugify('!!!') == ''
    assert slugify('___') == ''
    assert slugify('---') == ''
