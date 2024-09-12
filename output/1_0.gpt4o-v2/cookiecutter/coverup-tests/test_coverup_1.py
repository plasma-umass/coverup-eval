# file: cookiecutter/exceptions.py:149-154
# asked: {"lines": [149, 150], "branches": []}
# gained: {"lines": [149, 150], "branches": []}

import pytest
from cookiecutter.exceptions import RepositoryCloneFailed

def test_repository_clone_failed():
    with pytest.raises(RepositoryCloneFailed):
        raise RepositoryCloneFailed("Cannot clone the repository")

