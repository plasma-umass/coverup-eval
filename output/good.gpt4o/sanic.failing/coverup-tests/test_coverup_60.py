# file sanic/exceptions.py:86-91
# lines [86, 87, 91]
# branches []

import pytest
from sanic.exceptions import ServerError

class URLBuildError(ServerError):
    """
    **Status**: 500 Internal Server Error
    """
    pass

def test_url_build_error():
    with pytest.raises(URLBuildError) as exc_info:
        raise URLBuildError("URL build failed")
    
    assert exc_info.value.status_code == 500
    assert str(exc_info.value) == "URL build failed"
