# file string_utils/validation.py:177-201
# lines [177, 193, 194, 196, 198, 199, 201]
# branches ['193->194', '193->196', '198->199', '198->201']

import pytest
from string_utils.validation import is_url

def test_is_url_with_allowed_schemes():
    assert is_url('http://www.example.com', allowed_schemes=['http']) == True
    assert is_url('https://www.example.com', allowed_schemes=['https']) == True
    assert is_url('ftp://www.example.com', allowed_schemes=['ftp']) == True
    assert is_url('http://www.example.com', allowed_schemes=['https', 'ftp']) == False
    assert is_url('invalid://www.example.com', allowed_schemes=['http', 'https']) == False
    assert is_url('http://www.example.com', allowed_schemes=[]) == True
