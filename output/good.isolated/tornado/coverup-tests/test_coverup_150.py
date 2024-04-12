# file tornado/options.py:145-146
# lines [145, 146]
# branches []

import pytest
from tornado.options import OptionParser

class TestOptionParser:
    def test_normalize_name(self, mocker):
        # Setup
        parser = OptionParser()
        original_name = "test_option_name"
        expected_normalized_name = "test-option-name"

        # Exercise
        normalized_name = parser._normalize_name(original_name)

        # Verify
        assert normalized_name == expected_normalized_name

        # Cleanup - nothing to clean up as no external state was modified
