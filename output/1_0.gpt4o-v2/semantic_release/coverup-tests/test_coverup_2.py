# file: semantic_release/errors.py:26-27
# asked: {"lines": [26, 27], "branches": []}
# gained: {"lines": [26, 27], "branches": []}

import pytest
from semantic_release.errors import HvcsRepoParseError, SemanticReleaseBaseError

def test_hvcs_repo_parse_error_is_instance_of_base_error():
    error_instance = HvcsRepoParseError()
    assert isinstance(error_instance, HvcsRepoParseError)
    assert isinstance(error_instance, SemanticReleaseBaseError)
