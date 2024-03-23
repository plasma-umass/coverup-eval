# file semantic_release/errors.py:22-23
# lines [22, 23]
# branches []

import pytest
from semantic_release.errors import CiVerificationError

def test_ci_verification_error():
    with pytest.raises(CiVerificationError) as excinfo:
        raise CiVerificationError("CI verification failed")

    assert str(excinfo.value) == "CI verification failed"
