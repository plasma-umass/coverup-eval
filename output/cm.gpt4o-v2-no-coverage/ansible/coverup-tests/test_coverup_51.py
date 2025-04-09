# file: lib/ansible/module_utils/common/parameters.py:347-369
# asked: {"lines": [347, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369], "branches": [[351, 352], [351, 355], [352, 353], [352, 354], [355, 356], [355, 359], [356, 0], [356, 357], [357, 356], [357, 358], [359, 360], [359, 363], [360, 0], [360, 361], [361, 360], [361, 362], [363, 365], [363, 366], [366, 367], [366, 369]]}
# gained: {"lines": [347, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369], "branches": [[351, 352], [351, 355], [352, 353], [352, 354], [355, 356], [355, 359], [356, 0], [356, 357], [357, 356], [357, 358], [359, 360], [359, 363], [360, 0], [360, 361], [361, 360], [361, 362], [363, 365], [363, 366], [366, 367], [366, 369]]}

import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.common.text.converters import to_native
from ansible.module_utils.common._collections_compat import Mapping
from ansible.module_utils.six import binary_type, integer_types, text_type

def test_return_datastructure_name_string():
    result = list(_return_datastructure_name("test"))
    assert result == ["test"]

def test_return_datastructure_name_empty_string():
    result = list(_return_datastructure_name(""))
    assert result == []

def test_return_datastructure_name_mapping():
    class TestMapping(Mapping):
        def __init__(self, data):
            self.data = data

        def __getitem__(self, key):
            return self.data[key]

        def __iter__(self):
            return iter(self.data)

        def __len__(self):
            return len(self.data)

        def items(self):
            return self.data.items()

    test_mapping = TestMapping({"key": "value"})
    result = list(_return_datastructure_name(test_mapping))
    assert result == ["value"]

def test_return_datastructure_name_iterable():
    result = list(_return_datastructure_name(["test1", "test2"]))
    assert result == ["test1", "test2"]

def test_return_datastructure_name_bool():
    result = list(_return_datastructure_name(True))
    assert result == []

def test_return_datastructure_name_none():
    result = list(_return_datastructure_name(None))
    assert result == []

def test_return_datastructure_name_integer():
    result = list(_return_datastructure_name(42))
    assert result == ["42"]

def test_return_datastructure_name_float():
    result = list(_return_datastructure_name(3.14))
    assert result == ["3.14"]

def test_return_datastructure_name_unknown_type():
    class UnknownType:
        pass

    with pytest.raises(TypeError, match="Unknown parameter type: <class '.*UnknownType'>"):
        list(_return_datastructure_name(UnknownType()))
