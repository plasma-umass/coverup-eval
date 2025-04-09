# file sanic/helpers.py:113-115
# lines [113, 115]
# branches []

import pytest
from sanic.helpers import is_entity_header

def test_is_entity_header(mocker):
    # Mock the _ENTITY_HEADERS to control the test environment
    mocker.patch('sanic.helpers._ENTITY_HEADERS', new_callable=set)
    
    # Test with a header that is not in the mocked _ENTITY_HEADERS
    assert not is_entity_header("Content-Length")
    
    # Add the header to the mocked _ENTITY_HEADERS
    mocker.patch('sanic.helpers._ENTITY_HEADERS', new={"content-length"})
    
    # Test with a header that is now in the mocked _ENTITY_HEADERS
    assert is_entity_header("Content-Length")
