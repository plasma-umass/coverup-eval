# file semantic_release/errors.py:6-7
# lines [6, 7]
# branches []

import pytest
from semantic_release.errors import SemanticReleaseBaseError

def test_semantic_release_base_error():
    with pytest.raises(SemanticReleaseBaseError) as exc_info:
        raise SemanticReleaseBaseError("An error occurred")

    assert str(exc_info.value) == "An error occurred", "The exception message should match the expected message"
