# file: semantic_release/errors.py:18-19
# asked: {"lines": [18, 19], "branches": []}
# gained: {"lines": [18, 19], "branches": []}

import pytest
from semantic_release.errors import GitError, SemanticReleaseBaseError

def test_git_error_is_instance_of_base_error():
    error_instance = GitError()
    assert isinstance(error_instance, GitError)
    assert isinstance(error_instance, SemanticReleaseBaseError)
