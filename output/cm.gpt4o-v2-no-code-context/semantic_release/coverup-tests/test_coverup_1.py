# file: semantic_release/ci_checks.py:9-27
# asked: {"lines": [9, 18, 19, 20, 21, 22, 23, 24, 27], "branches": []}
# gained: {"lines": [9, 18, 19, 20, 21, 22, 23, 24, 27], "branches": []}

import pytest
from semantic_release.ci_checks import checker, CiVerificationError

def test_checker_decorator_success():
    @checker
    def always_passes():
        assert True

    assert always_passes() == True

def test_checker_decorator_failure():
    @checker
    def always_fails():
        assert False

    with pytest.raises(CiVerificationError, match="The verification check for the environment did not pass."):
        always_fails()
