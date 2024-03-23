# file lib/ansible/playbook/base.py:858-869
# lines [858, 861, 862, 863, 864, 865, 866, 867, 868, 869]
# branches []

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
def base_instance():
    return Base()

def test_get_path_with_direct_ds(base_instance, mocker):
    mock_ds = MockDataSource('test_file.yml', 42)
    base_instance._ds = mock_ds
    path = base_instance.get_path()
    assert path == 'test_file.yml:42'

def test_get_path_with_parent_ds(base_instance, mocker):
    mock_ds = MockDataSource('test_file.yml', 42)
    mock_play = MockPlay(mock_ds)
    mock_parent = MockParent(mock_play)
    base_instance._parent = mock_parent
    path = base_instance.get_path()
    assert path == 'test_file.yml:42'

def test_get_path_with_no_ds(base_instance):
    path = base_instance.get_path()
    assert path == ""
