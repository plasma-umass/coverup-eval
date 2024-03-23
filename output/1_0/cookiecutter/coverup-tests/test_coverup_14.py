# file cookiecutter/exceptions.py:85-90
# lines [85, 86]
# branches []

import pytest
from cookiecutter.exceptions import OutputDirExistsException

def test_output_dir_exists_exception():
    with pytest.raises(OutputDirExistsException) as exc_info:
        raise OutputDirExistsException("Output directory exists")

    assert str(exc_info.value) == "Output directory exists"
