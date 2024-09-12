# file: cookiecutter/exceptions.py:32-38
# asked: {"lines": [32, 33], "branches": []}
# gained: {"lines": [32, 33], "branches": []}

import pytest
from cookiecutter.exceptions import MissingProjectDir

def test_missing_project_dir():
    with pytest.raises(MissingProjectDir) as exc_info:
        raise MissingProjectDir("Generated project directory is missing.")
    assert str(exc_info.value) == "Generated project directory is missing."
