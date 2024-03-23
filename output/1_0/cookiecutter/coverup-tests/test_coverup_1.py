# file cookiecutter/exceptions.py:61-66
# lines [61, 62]
# branches []

import pytest

from cookiecutter.exceptions import UnknownRepoType

def test_unknown_repo_type_exception():
    with pytest.raises(UnknownRepoType) as exc_info:
        raise UnknownRepoType("Unknown repository type")

    assert str(exc_info.value) == "Unknown repository type"
