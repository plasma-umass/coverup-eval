# file: pysnooper/variables.py:124-133
# asked: {"lines": [124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127], [126, 128], [128, 129], [128, 131]]}
# gained: {"lines": [124, 125, 126, 127, 128, 129, 131, 133], "branches": [[126, 127], [126, 128], [128, 129], [128, 131]]}

import pytest
from collections.abc import Mapping, Sequence
from pysnooper.variables import Exploding, BaseVariable

class DummyMapping(Mapping):
    def __init__(self, **kwargs):
        self._data = kwargs

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

class DummySequence(Sequence):
    def __init__(self, *args):
        self._data = args

    def __getitem__(self, index):
        return self._data[index]

    def __len__(self):
        return len(self._data)

class DummyBaseVariable(BaseVariable):
    def _items(self, key, normalize=False):
        return [(key, normalize)]

def test_exploding_items_with_mapping(monkeypatch):
    monkeypatch.setattr('pysnooper.variables.Keys', DummyBaseVariable)
    source = 'dummy_source'
    exclude = ()
    expl = Exploding(source, exclude)
    mapping = DummyMapping(a=1, b=2)
    result = expl._items(mapping)
    assert result == [(mapping, False)]

def test_exploding_items_with_sequence(monkeypatch):
    monkeypatch.setattr('pysnooper.variables.Indices', DummyBaseVariable)
    source = 'dummy_source'
    exclude = ()
    expl = Exploding(source, exclude)
    sequence = DummySequence(1, 2, 3)
    result = expl._items(sequence)
    assert result == [(sequence, False)]

def test_exploding_items_with_other(monkeypatch):
    monkeypatch.setattr('pysnooper.variables.Attrs', DummyBaseVariable)
    source = 'dummy_source'
    exclude = ()
    expl = Exploding(source, exclude)
    other = object()
    result = expl._items(other)
    assert result == [(other, False)]
