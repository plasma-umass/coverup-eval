# file: pysnooper/variables.py:124-133
# asked: {"lines": [124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127], [126, 128], [128, 129], [128, 131]]}
# gained: {"lines": [124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127], [126, 128], [128, 129], [128, 131]]}

import pytest
from collections.abc import Mapping, Sequence
from pysnooper.variables import Exploding, BaseVariable, Keys, Indices, Attrs
from pysnooper.utils import ensure_tuple

class MockMapping(Mapping):
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

class MockSequence(Sequence):
    def __init__(self, *args):
        self._data = args

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

class MockSource:
    def __str__(self):
        return "mock_source"

class TestExploding:
    @pytest.fixture
    def setup_exploding(self):
        source = str(MockSource())
        exclude = ()
        return Exploding(source, exclude)

    def test_items_with_mapping(self, setup_exploding, mocker):
        mock_mapping = MockMapping(a=1, b=2)
        mock_keys = mocker.patch.object(Keys, '_items', return_value='mocked_keys')
        result = setup_exploding._items(mock_mapping)
        mock_keys.assert_called_once_with(mock_mapping, False)
        assert result == 'mocked_keys'

    def test_items_with_sequence(self, setup_exploding, mocker):
        mock_sequence = MockSequence(1, 2, 3)
        mock_indices = mocker.patch.object(Indices, '_items', return_value='mocked_indices')
        result = setup_exploding._items(mock_sequence)
        mock_indices.assert_called_once_with(mock_sequence, False)
        assert result == 'mocked_indices'

    def test_items_with_other(self, setup_exploding, mocker):
        mock_other = object()
        mock_attrs = mocker.patch.object(Attrs, '_items', return_value='mocked_attrs')
        result = setup_exploding._items(mock_other)
        mock_attrs.assert_called_once_with(mock_other, False)
        assert result == 'mocked_attrs'
