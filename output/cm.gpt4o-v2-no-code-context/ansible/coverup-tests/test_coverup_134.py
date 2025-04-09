# file: lib/ansible/executor/powershell/module_manifest.py:142-162
# asked: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}
# gained: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.module_utils._text import to_text, to_native, to_bytes
import pkgutil

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder.exec_scripts = {}
    return finder

def test_scan_exec_script_existing_key(ps_module_dep_finder):
    ps_module_dep_finder.exec_scripts['test_script'] = b'some_data'
    ps_module_dep_finder.scan_exec_script('test_script')
    assert ps_module_dep_finder.exec_scripts['test_script'] == b'some_data'

def test_scan_exec_script_no_data(ps_module_dep_finder):
    with patch('pkgutil.get_data', return_value=None):
        with pytest.raises(AnsibleError, match="Could not find executor powershell script for 'test_script'"):
            ps_module_dep_finder.scan_exec_script('test_script')

def test_scan_exec_script_with_data_debug_on(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.C.DEFAULT_DEBUG', True)
    mock_data = b'# some comment\nWrite-Output "Hello World"'
    with patch('pkgutil.get_data', return_value=mock_data):
        with patch.object(ps_module_dep_finder, 'scan_module') as mock_scan_module:
            ps_module_dep_finder.scan_exec_script('test_script')
            assert ps_module_dep_finder.exec_scripts['test_script'] == to_bytes(mock_data)
            mock_scan_module.assert_called_once_with(mock_data, wrapper=True, powershell=True)

def test_scan_exec_script_with_data_debug_off(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.executor.powershell.module_manifest.C.DEFAULT_DEBUG', False)
    mock_data = b'# some comment\nWrite-Output "Hello World"'
    stripped_data = b'Write-Output "Hello World"'
    with patch('pkgutil.get_data', return_value=mock_data):
        with patch('ansible.executor.powershell.module_manifest._strip_comments', return_value=stripped_data) as mock_strip_comments:
            with patch.object(ps_module_dep_finder, 'scan_module') as mock_scan_module:
                ps_module_dep_finder.scan_exec_script('test_script')
                assert ps_module_dep_finder.exec_scripts['test_script'] == to_bytes(stripped_data)
                mock_strip_comments.assert_called_once_with(mock_data)
                mock_scan_module.assert_called_once_with(mock_data, wrapper=True, powershell=True)
