# file sanic/exceptions.py:234-249
# lines [234, 244, 245, 247, 248, 249]
# branches ['244->245', '244->248']

import pytest
from sanic.exceptions import abort, SanicException
from sanic.helpers import STATUS_CODES

def test_abort_with_message():
    with pytest.raises(SanicException) as exc_info:
        abort(400, "Custom error message")
    assert exc_info.value.status_code == 400
    assert str(exc_info.value) == "Custom error message"

def test_abort_without_message(mocker):
    mocker.patch.dict(STATUS_CODES, {404: b"Not Found"})
    with pytest.raises(SanicException) as exc_info:
        abort(404)
    assert exc_info.value.status_code == 404
    assert str(exc_info.value) == "Not Found"
