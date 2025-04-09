# file: pymonet/either.py:22-35
# asked: {"lines": [22, 33, 34, 35], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [22, 33, 34, 35], "branches": [[33, 34], [33, 35]]}

import pytest
from pymonet.either import Either

class TestEither:
    def test_case_success(self):
        either = Either(10)
        either.is_right = lambda: True
        result = either.case(lambda x: x * 2, lambda x: x + 2)
        assert result == 12

    def test_case_error(self):
        either = Either(10)
        either.is_right = lambda: False
        result = either.case(lambda x: x * 2, lambda x: x + 2)
        assert result == 20
