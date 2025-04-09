# file: lib/ansible/executor/powershell/module_manifest.py:142-162
# asked: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}
# gained: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_scan_exec_script_existing_key(ps_module_dep_finder):
    ps_module_dep_finder.exec_scripts = {'existing_script': b'some_data'}
    ps_module_dep_finder.scan_exec_script('existing_script')
    assert ps_module_dep_finder.exec_scripts['existing_script'] == b'some_data'

def test_scan_exec_script_no_data(ps_module_dep_finder):
    with patch('pkgutil.get_data', return_value=None):
        with pytest.raises(AnsibleError, match="Could not find executor powershell script for 'non_existent_script'"):
            ps_module_dep_finder.scan_exec_script('non_existent_script')

def test_scan_exec_script_with_data(ps_module_dep_finder):
    mock_data = b'# some comment\nWrite-Output "Hello World"'
    ps_module_dep_finder.exec_scripts = {}
    with patch('pkgutil.get_data', return_value=mock_data):
        with patch('ansible.executor.powershell.module_manifest.to_bytes', side_effect=lambda x: x):
            with patch('ansible.executor.powershell.module_manifest.to_native', side_effect=lambda x: x):
                with patch('ansible.executor.powershell.module_manifest.to_text', side_effect=lambda x: x):
                    with patch('ansible.executor.powershell.module_manifest._strip_comments', return_value=b'Write-Output "Hello World"'):
                        with patch('ansible.executor.powershell.module_manifest.C.DEFAULT_DEBUG', False):
                            ps_module_dep_finder.scan_exec_script('test_script')
                            assert ps_module_dep_finder.exec_scripts['test_script'] == b'Write-Output "Hello World"'

def test_scan_exec_script_with_debug(ps_module_dep_finder):
    mock_data = b'# some comment\nWrite-Output "Hello World"'
    ps_module_dep_finder.exec_scripts = {}
    with patch('pkgutil.get_data', return_value=mock_data):
        with patch('ansible.executor.powershell.module_manifest.to_bytes', side_effect=lambda x: x):
            with patch('ansible.executor.powershell.module_manifest.to_native', side_effect=lambda x: x):
                with patch('ansible.executor.powershell.module_manifest.to_text', side_effect=lambda x: x):
                    with patch('ansible.executor.powershell.module_manifest.C.DEFAULT_DEBUG', True):
                        ps_module_dep_finder.scan_exec_script('test_script')
                        assert ps_module_dep_finder.exec_scripts['test_script'] == mock_data
