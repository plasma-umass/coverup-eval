# file sanic/exceptions.py:86-91
# lines [86, 87, 91]
# branches []

import pytest
from sanic.exceptions import URLBuildError

def test_url_build_error():
    with pytest.raises(URLBuildError) as exc_info:
        raise URLBuildError("Test URL build error")

    assert exc_info.type is URLBuildError
    assert str(exc_info.value) == "Test URL build error"
