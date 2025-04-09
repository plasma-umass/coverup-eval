# file sanic/exceptions.py:127-132
# lines [127, 128, 132]
# branches []

import pytest
from sanic.exceptions import InvalidUsage, HeaderNotFound

def test_header_not_found_exception():
    with pytest.raises(HeaderNotFound) as exc_info:
        raise HeaderNotFound("Header not found")
    
    assert exc_info.value.status_code == 400
    assert str(exc_info.value) == "Header not found"
