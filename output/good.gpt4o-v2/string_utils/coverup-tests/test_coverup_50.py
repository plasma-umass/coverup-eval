# file: string_utils/manipulation.py:462-497
# asked: {"lines": [485, 486, 489, 492, 495, 497], "branches": [[485, 486], [485, 489]]}
# gained: {"lines": [485, 486, 489, 492, 495, 497], "branches": [[485, 486], [485, 489]]}

import pytest
from string_utils.manipulation import slugify
from string_utils.errors import InvalidInputError

def test_slugify_with_non_string_input():
    with pytest.raises(InvalidInputError) as excinfo:
        slugify(12345)
    assert str(excinfo.value) == 'Expected "str", received "int"'

def test_slugify_with_string_input():
    result = slugify('Top 10 Reasons To Love Dogs!!!')
    assert result == 'top-10-reasons-to-love-dogs'

def test_slugify_with_special_characters():
    result = slugify('Mönstér Mägnët')
    assert result == 'monster-magnet'
