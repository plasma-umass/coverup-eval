# file: lib/ansible/executor/powershell/module_manifest.py:142-162
# asked: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}
# gained: {"lines": [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162], "branches": [[146, 147], [146, 149], [150, 151], [150, 154], [157, 158], [157, 160]]}

import pytest
import pkgutil
from ansible import constants as C
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.executor.powershell.module_manifest import PSModuleDepFinder

# Mock data for testing
MOCK_SCRIPT_NAME = 'test_script'
MOCK_SCRIPT_CONTENT = b'# This is a comment\nWrite-Output "Hello World"\n<# Block comment\nstill block comment\n#>\nWrite-Output "Another line"\n'

@pytest.fixture
def ps_module_dep_finder(monkeypatch):
    finder = PSModuleDepFinder()
    finder.exec_scripts = {}

    def mock_get_data(package, resource):
        if resource == to_native(MOCK_SCRIPT_NAME + '.ps1'):
            return MOCK_SCRIPT_CONTENT
        return None

    monkeypatch.setattr(pkgutil, 'get_data', mock_get_data)
    return finder

def test_scan_exec_script_existing_script(ps_module_dep_finder):
    ps_module_dep_finder.exec_scripts[MOCK_SCRIPT_NAME] = b'existing script'
    ps_module_dep_finder.scan_exec_script(MOCK_SCRIPT_NAME)
    assert ps_module_dep_finder.exec_scripts[MOCK_SCRIPT_NAME] == b'existing script'

def test_scan_exec_script_script_not_found(ps_module_dep_finder):
    with pytest.raises(AnsibleError, match="Could not find executor powershell script for 'non_existent_script'"):
        ps_module_dep_finder.scan_exec_script('non_existent_script')

def test_scan_exec_script_debug_mode(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_DEBUG', True)
    ps_module_dep_finder.scan_exec_script(MOCK_SCRIPT_NAME)
    assert ps_module_dep_finder.exec_scripts[MOCK_SCRIPT_NAME] == to_bytes(MOCK_SCRIPT_CONTENT)

def test_scan_exec_script_strip_comments(ps_module_dep_finder, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_DEBUG', False)
    ps_module_dep_finder.scan_exec_script(MOCK_SCRIPT_NAME)
    expected_content = b'Write-Output "Hello World"\nWrite-Output "Another line"'
    assert ps_module_dep_finder.exec_scripts[MOCK_SCRIPT_NAME] == to_bytes(expected_content)
