# file: string_utils/validation.py:177-201
# asked: {"lines": [193, 194, 196, 198, 199, 201], "branches": [[193, 194], [193, 196], [198, 199], [198, 201]]}
# gained: {"lines": [193, 194, 196, 198, 199, 201], "branches": [[193, 194], [193, 196], [198, 199], [198, 201]]}

import pytest
from string_utils.validation import is_url

def test_is_url_with_non_string():
    assert not is_url(None)
    assert not is_url(123)
    assert not is_url([])

def test_is_url_with_empty_string():
    assert not is_url('')
    assert not is_url(' ')

def test_is_url_with_invalid_url():
    assert not is_url('.mysite.com')

def test_is_url_with_valid_url():
    assert is_url('http://www.mysite.com')
    assert is_url('https://mysite.com')

def test_is_url_with_allowed_schemes():
    assert is_url('http://www.mysite.com', allowed_schemes=['http'])
    assert not is_url('ftp://www.mysite.com', allowed_schemes=['http'])
    assert is_url('ftp://www.mysite.com', allowed_schemes=['http', 'ftp'])
