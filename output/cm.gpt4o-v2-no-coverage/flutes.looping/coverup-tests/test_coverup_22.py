# file: flutes/iterator.py:352-357
# asked: {"lines": [352, 353, 354, 355, 356, 357], "branches": [[353, 354], [353, 355], [355, 356], [355, 357]]}
# gained: {"lines": [352, 353, 354, 355, 356, 357], "branches": [[353, 354], [353, 355], [355, 356], [355, 357]]}

import pytest
from flutes.iterator import Range

class TestRange:
    def setup_method(self):
        # Setup a Range instance with necessary attributes
        self.range = Range(10)
        self.range.l = 0
        self.range.step = 1
        self.range.length = 10

    def test_getitem_with_slice(self):
        result = self.range[2:5]
        assert result == [2, 3, 4]

    def test_getitem_with_negative_index(self):
        result = self.range[-1]
        assert result == 9

    def test_getitem_with_positive_index(self):
        result = self.range[3]
        assert result == 3

    def teardown_method(self):
        # Clean up any state if necessary
        del self.range
