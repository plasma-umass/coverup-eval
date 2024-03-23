# file cookiecutter/exceptions.py:149-154
# lines [149, 150]
# branches []

import pytest
from cookiecutter.exceptions import RepositoryCloneFailed

def test_repository_clone_failed_exception():
    with pytest.raises(RepositoryCloneFailed) as exc_info:
        raise RepositoryCloneFailed("Cloning failed")

    assert str(exc_info.value) == "Cloning failed"
