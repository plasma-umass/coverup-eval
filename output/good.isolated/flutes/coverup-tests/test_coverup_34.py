# file flutes/iterator.py:352-357
# lines [352, 353, 354, 355, 356, 357]
# branches ['353->354', '353->355', '355->356', '355->357']

import pytest
from flutes.iterator import Range

class TestRange:
    class MockRange(Range):
        def __init__(self, length):
            self.length = length

        def _get_idx(self, item):
            if item >= self.length or item < 0:
                raise IndexError("Index out of range")
            return item

    @pytest.fixture
    def mock_range(self):
        return self.MockRange(10)

    def test_getitem_with_positive_index(self, mock_range):
        assert mock_range[1] == 1

    def test_getitem_with_negative_index(self, mock_range):
        assert mock_range[-1] == 9

    def test_getitem_with_slice(self, mock_range):
        assert mock_range[1:5] == [1, 2, 3, 4]

    def test_getitem_with_full_slice(self, mock_range):
        assert mock_range[:] == list(range(10))

    def test_getitem_with_extended_slice(self, mock_range):
        assert mock_range[1:9:2] == [1, 3, 5, 7]

    def test_getitem_with_negative_slice(self, mock_range):
        assert mock_range[-5:-1] == [5, 6, 7, 8]

    def test_getitem_with_negative_step_slice(self, mock_range):
        assert mock_range[8:3:-1] == [8, 7, 6, 5, 4]

    def test_getitem_with_invalid_index(self, mock_range):
        with pytest.raises(IndexError):
            _ = mock_range[10]

    def test_getitem_with_invalid_negative_index(self, mock_range):
        with pytest.raises(IndexError):
            _ = mock_range[-11]
