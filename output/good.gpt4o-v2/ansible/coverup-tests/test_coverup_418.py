# file: lib/ansible/playbook/base.py:858-869
# asked: {"lines": [858, 861, 862, 863, 864, 865, 866, 867, 868, 869], "branches": []}
# gained: {"lines": [858, 861, 862, 863, 864, 865, 866, 867, 868, 869], "branches": []}

import pytest
from unittest.mock import Mock

from ansible.playbook.base import Base

@pytest.fixture
def base_instance():
    return Base()

def test_get_path_with_ds(base_instance):
    base_instance._ds = Mock()
    base_instance._ds._data_source = "source"
    base_instance._ds._line_number = 42

    path = base_instance.get_path()
    assert path == "source:42"

def test_get_path_with_parent_play_ds(base_instance):
    base_instance._ds = None
    base_instance._parent = Mock()
    base_instance._parent._play._ds._data_source = "parent_source"
    base_instance._parent._play._ds._line_number = 84

    path = base_instance.get_path()
    assert path == "parent_source:84"

def test_get_path_with_no_ds_or_parent_play_ds(base_instance):
    base_instance._ds = None
    base_instance._parent = Mock()
    base_instance._parent._play._ds = None

    path = base_instance.get_path()
    assert path == ""
