# file sanic/exceptions.py:172-174
# lines [172, 173, 174]
# branches []

import pytest
from sanic.exceptions import PyFileError

def test_pyfileerror_exception():
    file_name = "config.py"
    with pytest.raises(PyFileError) as exc_info:
        raise PyFileError(file_name)
    
    assert exc_info.value.args == ("could not execute config file %s", file_name)
