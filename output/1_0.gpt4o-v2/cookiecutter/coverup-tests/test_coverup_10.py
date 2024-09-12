# file: cookiecutter/exceptions.py:61-66
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from cookiecutter.exceptions import UnknownRepoType, CookiecutterException

def test_unknown_repo_type():
    with pytest.raises(UnknownRepoType) as exc_info:
        raise UnknownRepoType("Unknown repository type")
    assert str(exc_info.value) == "Unknown repository type"
    assert isinstance(exc_info.value, CookiecutterException)
