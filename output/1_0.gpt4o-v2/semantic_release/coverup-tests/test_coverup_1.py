# file: semantic_release/errors.py:22-23
# asked: {"lines": [22, 23], "branches": []}
# gained: {"lines": [22, 23], "branches": []}

import pytest
from semantic_release.errors import CiVerificationError

def test_ci_verification_error():
    with pytest.raises(CiVerificationError):
        raise CiVerificationError("CI verification failed")
