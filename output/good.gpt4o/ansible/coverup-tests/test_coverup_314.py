# file lib/ansible/plugins/loader.py:307-314
# lines [307, 308, 309, 310, 311, 312, 313, 314]
# branches ['310->311', '310->314', '311->310', '311->312', '312->310', '312->313']

import os
import pytest
from unittest import mock
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def mock_os_walk():
    with mock.patch('os.walk') as mock_walk:
        yield mock_walk

class TestPluginLoader(PluginLoader):
    def __init__(self):
        pass

def test_all_directories_with_init_py(mock_os_walk):
    mock_os_walk.return_value = [
        ('/testdir', ['subdir1', 'subdir2'], ['__init__.py']),
        ('/testdir/subdir1', [], []),
        ('/testdir/subdir2', [], [])
    ]

    loader = TestPluginLoader()
    result = loader._all_directories('/testdir')

    expected = [
        '/testdir',
        '/testdir/subdir1',
        '/testdir/subdir2'
    ]

    assert result == expected

def test_all_directories_without_init_py(mock_os_walk):
    mock_os_walk.return_value = [
        ('/testdir', ['subdir1', 'subdir2'], []),
        ('/testdir/subdir1', [], []),
        ('/testdir/subdir2', [], [])
    ]

    loader = TestPluginLoader()
    result = loader._all_directories('/testdir')

    expected = [
        '/testdir'
    ]

    assert result == expected
