# file semantic_release/errors.py:18-19
# lines [18, 19]
# branches []

import pytest
from semantic_release.errors import GitError

def test_git_error():
    with pytest.raises(GitError) as exc_info:
        raise GitError("An error occurred with Git")

    assert str(exc_info.value) == "An error occurred with Git"
