# file: lib/ansible/plugins/loader.py:331-382
# asked: {"lines": [331, 337, 338, 340, 343, 344, 345, 346, 347, 348, 349, 350, 351, 353, 354, 355, 360, 378, 381, 382], "branches": [[337, 338], [337, 340], [343, 344], [343, 360], [344, 345], [344, 360], [346, 347], [346, 353], [348, 349], [348, 353], [350, 348], [350, 351], [354, 344], [354, 355]]}
# gained: {"lines": [331, 337, 340, 343, 344, 345, 346, 347, 348, 349, 350, 351, 353, 354, 355, 360, 378, 381, 382], "branches": [[337, 340], [343, 344], [344, 345], [344, 360], [346, 347], [348, 349], [348, 353], [350, 351], [354, 355]]}

import pytest
import glob
import os
from unittest.mock import MagicMock, patch
from ansible.plugins.loader import PluginLoader, PluginPathContext

@pytest.fixture
def plugin_loader():
    loader = PluginLoader(
        class_name='test_class',
        package='test_package',
        config=['/config/dir1', '/config/dir2'],
        subdir='test_subdir'
    )
    loader._paths = None
    loader._extra_dirs = ['/extra/dir1', '/extra/dir2']
    return loader

def test_get_paths_with_context(plugin_loader, monkeypatch):
    mock_isdir = MagicMock(side_effect=lambda x: x in ['/config/dir1/subdir', '/config/dir2/subdir'])
    mock_glob = MagicMock(side_effect=lambda x: {
        '/config/dir1/*': ['/config/dir1/subdir'],
        '/config/dir1/*/*': [],
        '/config/dir2/*': ['/config/dir2/subdir'],
        '/config/dir2/*/*': []
    }[x])
    mock_get_package_paths = MagicMock(return_value=['/package/path1', '/package/path2/windows'])

    monkeypatch.setattr(glob, 'glob', mock_glob)
    monkeypatch.setattr(os.path, 'isdir', mock_isdir)
    monkeypatch.setattr(plugin_loader, '_get_package_paths', mock_get_package_paths)

    paths = plugin_loader._get_paths_with_context(subdirs=True)

    expected_paths = [
        PluginPathContext('/extra/dir1', False),
        PluginPathContext('/extra/dir2', False),
        PluginPathContext('/config/dir1/subdir', False),
        PluginPathContext('/config/dir1', False),
        PluginPathContext('/config/dir2/subdir', False),
        PluginPathContext('/config/dir2', False),
        PluginPathContext('/package/path1', True),
        PluginPathContext('/package/path2/windows', True)
    ]

    assert len(paths) == len(expected_paths)
    for path, expected in zip(paths, expected_paths):
        assert path.path == expected.path
        assert path.internal == expected.internal
    assert plugin_loader._paths == paths
