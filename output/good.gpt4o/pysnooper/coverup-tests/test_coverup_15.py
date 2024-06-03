# file pysnooper/variables.py:124-133
# lines [124, 125, 126, 127, 128, 129, 131, 133]
# branches ['126->127', '126->128', '128->129', '128->131']

import pytest
from unittest.mock import MagicMock, patch
from collections.abc import Mapping, Sequence
from pysnooper.variables import BaseVariable

class TestExploding:
    class Exploding(BaseVariable):
        def _items(self, main_value, normalize=False):
            if isinstance(main_value, Mapping):
                cls = TestExploding.Keys
            elif isinstance(main_value, Sequence):
                cls = TestExploding.Indices
            else:
                cls = TestExploding.Attrs

            return cls(self.source, self.exclude)._items(main_value, normalize)

    class Keys:
        def __init__(self, source, exclude):
            self.source = source
            self.exclude = exclude

        def _items(self, main_value, normalize):
            return 'keys_items'

    class Indices:
        def __init__(self, source, exclude):
            self.source = source
            self.exclude = exclude

        def _items(self, main_value, normalize):
            return 'indices_items'

    class Attrs:
        def __init__(self, source, exclude):
            self.source = source
            self.exclude = exclude

        def _items(self, main_value, normalize):
            return 'attrs_items'

    @patch.object(Keys, '_items', return_value='mapping_result')
    def test_items_mapping(self, mock_keys_items):
        obj = self.Exploding('source', 'exclude')
        result = obj._items({'key': 'value'}, normalize=True)

        mock_keys_items.assert_called_once_with({'key': 'value'}, True)
        assert result == 'mapping_result'

    @patch.object(Indices, '_items', return_value='sequence_result')
    def test_items_sequence(self, mock_indices_items):
        obj = self.Exploding('source', 'exclude')
        result = obj._items(['value1', 'value2'], normalize=False)

        mock_indices_items.assert_called_once_with(['value1', 'value2'], False)
        assert result == 'sequence_result'

    @patch.object(Attrs, '_items', return_value='other_result')
    def test_items_other(self, mock_attrs_items):
        obj = self.Exploding('source', 'exclude')
        result = obj._items(123, normalize=True)

        mock_attrs_items.assert_called_once_with(123, True)
        assert result == 'other_result'
