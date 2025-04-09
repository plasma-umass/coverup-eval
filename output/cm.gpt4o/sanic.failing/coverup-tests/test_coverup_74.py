# file sanic/exceptions.py:226-227
# lines [226, 227]
# branches []

import pytest
from sanic.exceptions import SanicException

class LoadFileException(SanicException):
    pass

def test_load_file_exception():
    with pytest.raises(LoadFileException) as exc_info:
        raise LoadFileException("File could not be loaded")
    
    assert str(exc_info.value) == "File could not be loaded"
    assert isinstance(exc_info.value, LoadFileException)
    assert isinstance(exc_info.value, SanicException)
