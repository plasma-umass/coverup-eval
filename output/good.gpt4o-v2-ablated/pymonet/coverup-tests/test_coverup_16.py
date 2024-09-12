# file: pymonet/monad_try.py:92-105
# asked: {"lines": [92, 103, 104, 105], "branches": [[103, 104], [103, 105]]}
# gained: {"lines": [92, 103, 104, 105], "branches": [[103, 104], [103, 105]]}

import pytest
from pymonet.monad_try import Try

class TestTry:
    def test_filter_success_true(self):
        # Arrange
        monad = Try(10, True)
        filterer = lambda x: x > 5

        # Act
        result = monad.filter(filterer)

        # Assert
        assert result.is_success
        assert result.value == 10

    def test_filter_success_false(self):
        # Arrange
        monad = Try(10, True)
        filterer = lambda x: x < 5

        # Act
        result = monad.filter(filterer)

        # Assert
        assert not result.is_success
        assert result.value == 10

    def test_filter_failure(self):
        # Arrange
        monad = Try(10, False)
        filterer = lambda x: x > 5

        # Act
        result = monad.filter(filterer)

        # Assert
        assert not result.is_success
        assert result.value == 10
