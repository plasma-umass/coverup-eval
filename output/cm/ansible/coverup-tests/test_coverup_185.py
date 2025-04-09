# file lib/ansible/executor/powershell/module_manifest.py:142-162
# lines [142, 145, 146, 147, 149, 150, 151, 152, 154, 157, 158, 160, 161, 162]
# branches ['146->147', '146->149', '150->151', '150->154', '157->158', '157->160']

import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.module_utils._text import to_bytes, to_text
from ansible import constants as C
import pkgutil

# Mocking pkgutil.get_data to control its return value
@pytest.fixture
def mock_pkgutil_get_data(mocker):
    return mocker.patch('pkgutil.get_data', return_value=None)

# Test function to cover the missing branch where data is None
def test_scan_exec_script_data_none(mock_pkgutil_get_data):
    dep_finder = PSModuleDepFinder()
    with pytest.raises(AnsibleError) as excinfo:
        dep_finder.scan_exec_script('non_existent_script')
    assert "Could not find executor powershell script for 'non_existent_script'" in str(excinfo.value)

# Test function to cover the branch where C.DEFAULT_DEBUG is True
def test_scan_exec_script_debug_mode(mocker):
    mocker.patch('pkgutil.get_data', return_value=b"# This is a comment\n$Data = 'Some data'")
    mocker.patch.object(C, 'DEFAULT_DEBUG', True)
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('existent_script')
    assert dep_finder.exec_scripts['existent_script'] == b"# This is a comment\n$Data = 'Some data'"

# Test function to cover the branch where C.DEFAULT_DEBUG is False
def test_scan_exec_script_non_debug_mode(mocker):
    mocker.patch('pkgutil.get_data', return_value=b"# This is a comment\n$Data = 'Some data'")
    mocker.patch.object(C, 'DEFAULT_DEBUG', False)
    dep_finder = PSModuleDepFinder()
    dep_finder.scan_exec_script('existent_script')
    # The assertion should not expect a newline at the start of the script
    assert dep_finder.exec_scripts['existent_script'] == b"$Data = 'Some data'"
