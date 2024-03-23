# file cookiecutter/exceptions.py:12-18
# lines [12, 13]
# branches []

import pytest
from cookiecutter.exceptions import NonTemplatedInputDirException

def test_non_templated_input_dir_exception():
    with pytest.raises(NonTemplatedInputDirException) as exc_info:
        raise NonTemplatedInputDirException("Input directory is not templated.")
    
    assert str(exc_info.value) == "Input directory is not templated."
