# file string_utils/manipulation.py:462-497
# lines [462, 485, 486, 489, 492, 495, 497]
# branches ['485->486', '485->489']

import pytest
from string_utils.manipulation import slugify, InvalidInputError
import re

# Mocking the dependencies
@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    global is_string, NO_LETTERS_OR_NUMBERS_RE, SPACES_RE, asciify
    is_string = mocker.patch('string_utils.manipulation.is_string', return_value=True)
    NO_LETTERS_OR_NUMBERS_RE = mocker.patch('string_utils.manipulation.NO_LETTERS_OR_NUMBERS_RE', re.compile(r'[^a-zA-Z0-9]'))
    SPACES_RE = mocker.patch('string_utils.manipulation.SPACES_RE', re.compile(r'\s+'))
    asciify = mocker.patch('string_utils.manipulation.asciify', side_effect=lambda x: x.encode('ascii', 'ignore').decode('ascii'))

def test_slugify_valid_input():
    assert slugify('Top 10 Reasons To Love Dogs!!!') == 'top-10-reasons-to-love-dogs'
    assert slugify('Monster Magnet') == 'monster-magnet'
    assert slugify('Hello, World!', '_') == 'hello_world'

def test_slugify_invalid_input(mocker):
    is_string.return_value = False
    with pytest.raises(InvalidInputError):
        slugify(12345)

def test_slugify_edge_cases():
    assert slugify('') == ''
    assert slugify('   ') == ''
    assert slugify('---') == ''
    assert slugify('a' * 1000) == 'a' * 1000
    assert slugify('a' * 1000, '_') == 'a' * 1000

def test_slugify_normalize_joins():
    assert slugify('a--b--c', '-') == 'a-b-c'
    assert slugify('a__b__c', '_') == 'a_b_c'
    assert slugify('a  b  c', '-') == 'a-b-c'
