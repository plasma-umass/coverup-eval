# file cookiecutter/exceptions.py:77-82
# lines [77, 78]
# branches []

import pytest
from cookiecutter.exceptions import ContextDecodingException

def test_context_decoding_exception():
    with pytest.raises(ContextDecodingException) as exc_info:
        raise ContextDecodingException("Test decoding exception")

    assert str(exc_info.value) == "Test decoding exception"
