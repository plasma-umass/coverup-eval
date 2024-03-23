# file sanic/exceptions.py:172-174
# lines [172, 173, 174]
# branches []

import pytest
from sanic.exceptions import PyFileError

def test_pyfileerror_exception():
    file_path = "nonexistent_config.py"
    with pytest.raises(PyFileError) as exc_info:
        raise PyFileError(file_path)
    
    expected_message = f"could not execute config file {file_path}"
    actual_message = exc_info.value.args[0] % exc_info.value.args[1]
    assert actual_message == expected_message
