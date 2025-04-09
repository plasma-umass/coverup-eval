# file: flutils/namedtupleutils.py:107-137
# asked: {"lines": [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137], "branches": [[113, 114], [113, 122], [114, 113], [114, 115], [120, 113], [120, 121], [122, 123], [122, 124], [125, 126], [125, 129], [129, 131], [129, 135]]}
# gained: {"lines": [107, 108, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, 133, 134, 135, 136, 137], "branches": [[113, 114], [113, 122], [114, 113], [114, 115], [120, 121], [122, 123], [122, 124], [125, 126], [125, 129], [129, 131], [129, 135]]}

import pytest
from collections import OrderedDict
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_mapping():
    # Test with a valid mapping
    data = OrderedDict([('key1', 'value1'), ('key2', 'value2')])
    result = _to_namedtuple(data)
    assert result.key1 == 'value1'
    assert result.key2 == 'value2'

    # Test with a mapping containing invalid identifiers
    data = OrderedDict([('key1', 'value1'), ('123', 'value2')])
    result = _to_namedtuple(data)
    assert hasattr(result, 'key1')
    assert not hasattr(result, '123')

    # Test with an empty mapping
    data = OrderedDict()
    result = _to_namedtuple(data)
    assert result == ()

    # Test with a mapping containing non-string keys
    data = OrderedDict([(1, 'value1'), (2, 'value2')])
    result = _to_namedtuple(data)
    assert result == ()

    # Test with a non-OrderedDict mapping
    data = {'key1': 'value1', 'key2': 'value2'}
    result = _to_namedtuple(data)
    assert result.key1 == 'value1'
    assert result.key2 == 'value2'

    # Test with a mapping containing keys that are not valid identifiers
    data = OrderedDict([('key1', 'value1'), ('key-2', 'value2')])
    result = _to_namedtuple(data)
    assert hasattr(result, 'key1')
    assert not hasattr(result, 'key-2')
