# file lib/ansible/executor/powershell/module_manifest.py:142-162
# lines [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162]
# branches ['146->147', '146->149', '150->151', '150->154', '157->158', '157->160']

import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_text, to_bytes
import ansible.constants as C

@pytest.fixture
def ps_module_dep_finder():
    finder = PSModuleDepFinder()
    finder.exec_scripts = {}
    return finder

@patch('ansible.executor.powershell.module_manifest.pkgutil.get_data')
@patch('ansible.executor.powershell.module_manifest._strip_comments')
def test_scan_exec_script(mock_strip_comments, mock_get_data, ps_module_dep_finder):
    script_name = 'test_script'
    script_content = 'Write-Host "Hello, World!"'
    mock_get_data.return_value = script_content.encode('utf-8')
    mock_strip_comments.return_value = script_content.encode('utf-8')

    # Test when script is already in exec_scripts
    ps_module_dep_finder.exec_scripts[script_name] = b'Existing script content'
    ps_module_dep_finder.scan_exec_script(script_name)
    assert ps_module_dep_finder.exec_scripts[script_name] == b'Existing script content'

    # Test when script is not found
    ps_module_dep_finder.exec_scripts = {}
    mock_get_data.return_value = None
    with pytest.raises(AnsibleError, match=f"Could not find executor powershell script for '{script_name}'"):
        ps_module_dep_finder.scan_exec_script(script_name)

    # Test when script is found and DEFAULT_DEBUG is True
    ps_module_dep_finder.exec_scripts = {}
    mock_get_data.return_value = script_content.encode('utf-8')
    C.DEFAULT_DEBUG = True
    ps_module_dep_finder.scan_exec_script(script_name)
    assert ps_module_dep_finder.exec_scripts[script_name] == to_bytes(script_content)

    # Test when script is found and DEFAULT_DEBUG is False
    ps_module_dep_finder.exec_scripts = {}
    C.DEFAULT_DEBUG = False
    ps_module_dep_finder.scan_exec_script(script_name)
    mock_strip_comments.assert_called_once_with(to_bytes(script_content))
    assert ps_module_dep_finder.exec_scripts[script_name] == to_bytes(script_content)

    # Clean up
    C.DEFAULT_DEBUG = False
