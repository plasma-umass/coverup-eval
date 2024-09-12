# file: semantic_release/errors.py:14-15
# asked: {"lines": [14, 15], "branches": []}
# gained: {"lines": [14, 15], "branches": []}

import pytest
from semantic_release.errors import UnknownCommitMessageStyleError, SemanticReleaseBaseError

def test_unknown_commit_message_style_error():
    with pytest.raises(UnknownCommitMessageStyleError):
        raise UnknownCommitMessageStyleError()

    assert issubclass(UnknownCommitMessageStyleError, SemanticReleaseBaseError)
