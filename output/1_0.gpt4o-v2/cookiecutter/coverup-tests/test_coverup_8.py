# file: cookiecutter/exceptions.py:141-146
# asked: {"lines": [141, 142], "branches": []}
# gained: {"lines": [141, 142], "branches": []}

import pytest
from cookiecutter.exceptions import RepositoryNotFound

def test_repository_not_found():
    with pytest.raises(RepositoryNotFound) as exc_info:
        raise RepositoryNotFound("Repository not found")
    assert str(exc_info.value) == "Repository not found"
