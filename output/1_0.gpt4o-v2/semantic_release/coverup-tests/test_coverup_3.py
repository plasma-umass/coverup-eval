# file: semantic_release/errors.py:6-7
# asked: {"lines": [6, 7], "branches": []}
# gained: {"lines": [6, 7], "branches": []}

import pytest
from semantic_release.errors import SemanticReleaseBaseError

def test_semantic_release_base_error():
    with pytest.raises(SemanticReleaseBaseError):
        raise SemanticReleaseBaseError("This is a test error")
