# file: lib/ansible/playbook/base.py:858-869
# asked: {"lines": [858, 861, 862, 863, 864, 865, 866, 867, 868, 869], "branches": []}
# gained: {"lines": [858, 861, 862, 863, 864, 865, 866, 867, 868, 869], "branches": []}

import pytest
from ansible.playbook.base import Base

class MockDataSource:
    def __init__(self, data_source, line_number):
        self._data_source = data_source
        self._line_number = line_number

class MockParent:
    def __init__(self, play):
        self._play = play

class MockPlay:
    def __init__(self, ds):
        self._ds = ds

@pytest.fixture
def base_with_ds():
    base = Base()
    base._ds = MockDataSource("test_path", 42)
    return base

@pytest.fixture
def base_with_parent_ds():
    base = Base()
    play = MockPlay(MockDataSource("parent_path", 84))
    base._parent = MockParent(play)
    return base

@pytest.fixture
def base_without_ds():
    return Base()

def test_get_path_with_ds(base_with_ds):
    assert base_with_ds.get_path() == "test_path:42"

def test_get_path_with_parent_ds(base_with_parent_ds):
    assert base_with_parent_ds.get_path() == "parent_path:84"

def test_get_path_without_ds_or_parent_ds(base_without_ds):
    assert base_without_ds.get_path() == ""
