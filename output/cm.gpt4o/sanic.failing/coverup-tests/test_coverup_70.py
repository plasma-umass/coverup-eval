# file sanic/helpers.py:113-115
# lines [113, 115]
# branches []

import pytest
from sanic.helpers import is_entity_header

def test_is_entity_header():
    # Assuming _ENTITY_HEADERS is a set of known entity headers
    _ENTITY_HEADERS = {"content-length", "content-type", "content-encoding"}

    # Mocking the _ENTITY_HEADERS in the sanic.helpers module
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr("sanic.helpers._ENTITY_HEADERS", _ENTITY_HEADERS)

        # Test with a header that is in _ENTITY_HEADERS
        assert is_entity_header("Content-Length") == True
        assert is_entity_header("content-type") == True

        # Test with a header that is not in _ENTITY_HEADERS
        assert is_entity_header("Authorization") == False
        assert is_entity_header("Host") == False

        # Test with a header that is in _ENTITY_HEADERS but with different casing
        assert is_entity_header("Content-Encoding") == True
        assert is_entity_header("CONTENT-TYPE") == True
