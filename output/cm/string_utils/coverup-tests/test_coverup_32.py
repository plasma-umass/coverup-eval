# file string_utils/manipulation.py:462-497
# lines [462, 485, 486, 489, 492, 495, 497]
# branches ['485->486', '485->489']

import pytest
from string_utils.manipulation import slugify
from string_utils.errors import InvalidInputError

def test_slugify_with_invalid_input(mocker):
    mocker.patch('string_utils.manipulation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        slugify('Invalid Input')

def test_slugify_with_special_characters():
    assert slugify('Hello, World!') == 'hello-world'
    assert slugify('Hello, World!', separator='_') == 'hello_world'
    assert slugify('   Multiple      Spaces   ') == 'multiple-spaces'
    assert slugify('Dashes---and___underscores') == 'dashes-and-underscores'
    assert slugify('Mönstér Mägnët') == 'monster-magnet'
    assert slugify('Text with numbers 12345') == 'text-with-numbers-12345'
    assert slugify('Text with punctuation!!!') == 'text-with-punctuation'
    assert slugify('Text with mixed-separators_and   spaces') == 'text-with-mixed-separators-and-spaces'
