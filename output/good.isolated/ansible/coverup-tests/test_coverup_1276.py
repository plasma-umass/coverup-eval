# file lib/ansible/playbook/base.py:858-869
# lines [861, 862, 863, 864, 865, 866, 867, 868, 869]
# branches []

import pytest
from ansible.playbook.base import Base

class MockDataSource:
    def __init__(self, data_source, line_number):
        self._data_source = data_source
        self._line_number = line_number

class MockParent:
    def __init__(self, data_source, line_number):
        self._play = MockPlay(data_source, line_number)

class MockPlay:
    def __init__(self, data_source, line_number):
        self._ds = MockDataSource(data_source, line_number)

@pytest.fixture
def base_instance():
    base = Base()
    yield base
    del base

def test_get_path_with_direct_ds(base_instance):
    base_instance._ds = MockDataSource('path/to/playbook.yml', 42)
    path = base_instance.get_path()
    assert path == 'path/to/playbook.yml:42'

def test_get_path_with_parent_ds(base_instance):
    base_instance._parent = MockParent('path/to/parent_playbook.yml', 101)
    path = base_instance.get_path()
    assert path == 'path/to/parent_playbook.yml:101'

def test_get_path_without_ds_or_parent(base_instance):
    path = base_instance.get_path()
    assert path == ""
