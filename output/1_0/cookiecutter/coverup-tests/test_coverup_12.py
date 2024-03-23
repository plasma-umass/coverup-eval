# file cookiecutter/exceptions.py:32-38
# lines [32, 33]
# branches []

import pytest
from cookiecutter.exceptions import MissingProjectDir

def test_missing_project_dir_exception():
    with pytest.raises(MissingProjectDir) as exc_info:
        raise MissingProjectDir("Test missing project directory exception.")

    assert str(exc_info.value) == "Test missing project directory exception."
