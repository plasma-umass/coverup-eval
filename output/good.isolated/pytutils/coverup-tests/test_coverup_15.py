# file pytutils/lazy/lazy_regex.py:202-206
# lines [202, 203, 204, 206]
# branches ['203->204', '203->206']

import pytest
from pytutils.lazy.lazy_regex import LazyRegex, finditer_public
import re

class TestLazyRegex:
    def test_finditer_public_with_lazy_regex(self, mocker):
        # Mocking the finditer method of a LazyRegex instance
        mock_finditer = mocker.MagicMock(return_value='expected_result')
        lazy_regex = LazyRegex('pattern', re.IGNORECASE)
        lazy_regex.finditer = mock_finditer

        # Call the function with a LazyRegex instance
        result = finditer_public(lazy_regex, 'string to search')

        # Assert that the mocked finditer method was called
        mock_finditer.assert_called_once_with('string to search')
        # Assert that the result is as expected
        assert result == 'expected_result'

    def test_finditer_public_with_non_lazy_regex(self):
        # Call the function with a non-LazyRegex pattern
        pattern = 'pattern'
        string = 'string to search pattern'
        flags = re.IGNORECASE
        result = finditer_public(pattern, string, flags)

        # Convert result to a list to be able to assert its content
        matches = list(result)

        # Assert that the result is a match iterator with the correct match
        assert len(matches) == 1
        assert matches[0].group() == 'pattern'
