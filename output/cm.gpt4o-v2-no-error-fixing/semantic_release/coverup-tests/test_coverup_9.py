# file: semantic_release/ci_checks.py:9-27
# asked: {"lines": [9, 18, 19, 20, 21, 22, 23, 24, 27], "branches": []}
# gained: {"lines": [9, 18, 19, 20, 21, 22, 23, 24, 27], "branches": []}

import pytest
from semantic_release.errors import CiVerificationError
from semantic_release.ci_checks import checker

def test_checker_decorator_pass():
    @checker
    def dummy_check():
        assert True

    assert dummy_check() is True

def test_checker_decorator_fail():
    @checker
    def dummy_check():
        assert False

    with pytest.raises(CiVerificationError, match="The verification check for the environment did not pass."):
        dummy_check()
