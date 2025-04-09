# file lib/ansible/module_utils/common/parameters.py:347-369
# lines [351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 365, 366, 367, 369]
# branches ['351->352', '351->355', '352->353', '352->354', '355->356', '355->359', '356->exit', '356->357', '357->356', '357->358', '359->360', '359->363', '360->exit', '360->361', '361->360', '361->362', '363->365', '363->366', '366->367', '366->369']

import pytest
from ansible.module_utils.common.parameters import _return_datastructure_name
from ansible.module_utils._text import to_native, text_type, binary_type
from collections.abc import Mapping
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.six import integer_types

def test_return_datastructure_name(mocker):
    # Mocking to_native to return the same value for simplicity
    mocker.patch('ansible.module_utils._text.to_native', side_effect=lambda x, **kwargs: x)

    # Test for text_type and binary_type
    assert list(_return_datastructure_name("test_string")) == ["test_string"]
    assert list(_return_datastructure_name(b"test_bytes")) == ["test_bytes"]

    # Test for Mapping
    assert list(_return_datastructure_name({"key": "value"})) == ["value"]

    # Test for iterable
    assert list(_return_datastructure_name(["item1", "item2"])) == ["item1", "item2"]

    # Test for bool and NoneType
    assert list(_return_datastructure_name(True)) == []
    assert list(_return_datastructure_name(None)) == []

    # Test for integer_types and float
    assert list(_return_datastructure_name(42)) == ["42"]
    assert list(_return_datastructure_name(3.14)) == ["3.14"]

    # Test for unknown type to raise TypeError
    with pytest.raises(TypeError, match="Unknown parameter type: <class 'complex'>"):
        list(_return_datastructure_name(1 + 2j))
