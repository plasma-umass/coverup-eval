# file: lib/ansible/template/native_helpers.py:23-43
# asked: {"lines": [23, 27, 28, 29, 30, 31, 32, 34, 41, 43], "branches": [[27, 28], [27, 30], [28, 29], [28, 43], [30, 31], [30, 34], [31, 32], [31, 43], [34, 41], [34, 43]]}
# gained: {"lines": [23, 27, 28, 29, 30, 31, 32, 34, 41, 43], "branches": [[27, 28], [27, 30], [28, 29], [30, 31], [30, 34], [31, 32], [34, 41], [34, 43]]}

import pytest
from jinja2.runtime import StrictUndefined
from ansible.module_utils.common.collections import is_sequence, Mapping
from ansible.template.native_helpers import _fail_on_undefined

def test_fail_on_undefined_with_mapping():
    class TestMapping(Mapping):
        def __init__(self, **kwargs):
            self._data = kwargs

        def __getitem__(self, key):
            return self._data[key]

        def __iter__(self):
            return iter(self._data)

        def __len__(self):
            return len(self._data)

        def values(self):
            return self._data.values()

    data = TestMapping(a=1, b=StrictUndefined(name='b'))
    with pytest.raises(Exception) as excinfo:
        _fail_on_undefined(data)
    assert 'b' in str(excinfo.value)

def test_fail_on_undefined_with_sequence():
    data = [1, StrictUndefined(name='item')]
    with pytest.raises(Exception) as excinfo:
        _fail_on_undefined(data)
    assert 'item' in str(excinfo.value)

def test_fail_on_undefined_with_strictundefined():
    data = StrictUndefined(name='data')
    with pytest.raises(Exception) as excinfo:
        _fail_on_undefined(data)
    assert 'data' in str(excinfo.value)

def test_fail_on_undefined_with_other():
    data = 42
    assert _fail_on_undefined(data) == 42
