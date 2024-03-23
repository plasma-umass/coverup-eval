# file semantic_release/errors.py:14-15
# lines [14, 15]
# branches []

import pytest
from semantic_release.errors import UnknownCommitMessageStyleError

def test_unknown_commit_message_style_error():
    with pytest.raises(UnknownCommitMessageStyleError) as excinfo:
        raise UnknownCommitMessageStyleError("An unknown commit message style error occurred.")
    assert "An unknown commit message style error occurred." in str(excinfo.value)
