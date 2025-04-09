# file sanic/exceptions.py:226-227
# lines [226, 227]
# branches []

import pytest
from sanic.exceptions import LoadFileException

def test_load_file_exception():
    with pytest.raises(LoadFileException) as exc_info:
        raise LoadFileException("Failed to load file", status_code=400)

    assert exc_info.value.args[0] == "Failed to load file"
    assert exc_info.value.status_code == 400
