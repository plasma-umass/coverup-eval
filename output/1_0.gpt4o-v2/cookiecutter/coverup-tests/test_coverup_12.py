# file: cookiecutter/exceptions.py:77-82
# asked: {"lines": [77, 78], "branches": []}
# gained: {"lines": [77, 78], "branches": []}

import pytest
from cookiecutter.exceptions import ContextDecodingException, CookiecutterException

def test_context_decoding_exception():
    with pytest.raises(ContextDecodingException) as exc_info:
        raise ContextDecodingException("Failed to decode JSON")
    
    assert str(exc_info.value) == "Failed to decode JSON"
    assert isinstance(exc_info.value, CookiecutterException)
    assert isinstance(exc_info.value, ContextDecodingException)
