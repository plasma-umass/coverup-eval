# file sanic/exceptions.py:127-132
# lines [127, 128, 132]
# branches []

import pytest
from sanic.exceptions import HeaderNotFound

def test_header_not_found_exception():
    with pytest.raises(HeaderNotFound) as exc_info:
        raise HeaderNotFound("Header is missing")

    assert exc_info.type is HeaderNotFound
    assert str(exc_info.value) == "Header is missing"
    assert exc_info.value.status_code == 400
