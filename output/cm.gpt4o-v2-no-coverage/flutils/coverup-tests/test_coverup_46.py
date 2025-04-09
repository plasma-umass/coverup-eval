# file: flutils/namedtupleutils.py:107-137
# asked: {"lines": [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137], "branches": [[113, 114], [113, 122], [114, 113], [114, 115], [120, 113], [120, 121], [122, 123], [122, 124], [125, 126], [125, 129], [129, 131], [129, 135]]}
# gained: {"lines": [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137], "branches": [[113, 114], [113, 122], [114, 115], [120, 121], [122, 123], [122, 124], [125, 126], [125, 129], [129, 131], [129, 135]]}

import pytest
from collections import OrderedDict
from collections.abc import Mapping
from typing import Any, NamedTuple, Tuple, Union
from flutils.namedtupleutils import _to_namedtuple
from flutils.validators import validate_identifier

class TestToNamedTuple:
    def test_empty_mapping(self):
        class EmptyMapping(Mapping):
            def __getitem__(self, key):
                raise KeyError

            def __iter__(self):
                return iter([])

            def __len__(self):
                return 0

        empty_mapping = EmptyMapping()
        result = _to_namedtuple(empty_mapping)
        assert isinstance(result, tuple) and not result

    def test_ordered_dict(self):
        ordered_dict = OrderedDict([('a', 1), ('b', 2)])
        result = _to_namedtuple(ordered_dict)
        assert isinstance(result, tuple)
        assert result.a == 1
        assert result.b == 2

    def test_unordered_dict(self):
        unordered_dict = {'b': 2, 'a': 1}
        result = _to_namedtuple(unordered_dict)
        assert isinstance(result, tuple)
        assert result.a == 1
        assert result.b == 2

    def test_invalid_identifier(self, mocker):
        mocker.patch('flutils.validators.validate_identifier', side_effect=SyntaxError)
        invalid_dict = {'1invalid': 1, 'valid': 2}
        result = _to_namedtuple(invalid_dict)
        assert isinstance(result, tuple)
        assert hasattr(result, 'valid')
        assert not hasattr(result, '1invalid')

    def test_nested_mapping(self):
        nested_dict = {'a': {'b': 2}}
        result = _to_namedtuple(nested_dict)
        assert isinstance(result, tuple)
        assert isinstance(result.a, tuple)
        assert result.a.b == 2

    def test_non_mapping(self):
        with pytest.raises(TypeError):
            _to_namedtuple(123)
