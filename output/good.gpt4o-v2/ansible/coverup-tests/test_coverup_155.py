# file: lib/ansible/executor/powershell/module_manifest.py:142-162
# asked: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}
# gained: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder.exec_scripts = {}
    return finder

def test_scan_exec_script_existing_script(ps_module_dep_finder):
    ps_module_dep_finder.exec_scripts['existing_script'] = b'some_data'
    ps_module_dep_finder.scan_exec_script('existing_script')
    assert ps_module_dep_finder.exec_scripts['existing_script'] == b'some_data'

def test_scan_exec_script_script_not_found(ps_module_dep_finder):
    with patch('pkgutil.get_data', return_value=None):
        with pytest.raises(AnsibleError, match="Could not find executor powershell script for 'non_existent_script'"):
            ps_module_dep_finder.scan_exec_script('non_existent_script')

def test_scan_exec_script_debug_mode(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.constants.DEFAULT_DEBUG', True)
    with patch('pkgutil.get_data', return_value=b'script_data'):
        ps_module_dep_finder.scan_exec_script('debug_script')
        assert ps_module_dep_finder.exec_scripts['debug_script'] == b'script_data'

def test_scan_exec_script_strip_comments(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr('ansible.constants.DEFAULT_DEBUG', False)
    with patch('pkgutil.get_data', return_value=b'script_data'):
        with patch('ansible.executor.powershell.module_manifest._strip_comments', return_value=b'stripped_data') as mock_strip_comments:
            ps_module_dep_finder.scan_exec_script('strip_script')
            mock_strip_comments.assert_called_once_with(b'script_data')
            assert ps_module_dep_finder.exec_scripts['strip_script'] == b'stripped_data'

def test_scan_exec_script_scan_module(ps_module_dep_finder):
    with patch('pkgutil.get_data', return_value=b'script_data'):
        with patch.object(ps_module_dep_finder, 'scan_module') as mock_scan_module:
            ps_module_dep_finder.scan_exec_script('module_script')
            mock_scan_module.assert_called_once_with(b'script_data', wrapper=True, powershell=True)
