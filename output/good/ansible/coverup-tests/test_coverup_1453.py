# file lib/ansible/executor/powershell/module_manifest.py:142-162
# lines [147]
# branches ['146->147']

import pytest
from ansible.errors import AnsibleError
from ansible.executor.powershell.module_manifest import PSModuleDepFinder
from ansible.module_utils._text import to_bytes, to_text
from ansible import constants as C

# Mock the necessary functions and constants
@pytest.fixture
def mock_pkgutil(mocker):
    return mocker.patch('ansible.executor.powershell.module_manifest.pkgutil.get_data', return_value=None)

@pytest.fixture
def mock_ansible_error(mocker):
    return mocker.patch('ansible.executor.powershell.module_manifest.AnsibleError')

@pytest.fixture
def mock_strip_comments(mocker):
    return mocker.patch('ansible.executor.powershell.module_manifest._strip_comments', return_value=b'')

@pytest.fixture
def ps_module_dep_finder():
    return PSModuleDepFinder()

def test_scan_exec_script_already_scanned(ps_module_dep_finder):
    # Pre-populate the exec_scripts to simulate the script already being scanned
    script_name = 'already_scanned_script'
    ps_module_dep_finder.exec_scripts[script_name] = b'some_data'

    # Call the method under test
    ps_module_dep_finder.scan_exec_script(script_name)

    # Assert that the method returned early as expected
    assert script_name in ps_module_dep_finder.exec_scripts
    assert ps_module_dep_finder.exec_scripts[script_name] == b'some_data'

def test_scan_exec_script_not_found(mock_pkgutil, ps_module_dep_finder):
    script_name = 'nonexistent_script'

    # Expect the AnsibleError to be raised when the script is not found
    with pytest.raises(AnsibleError):
        ps_module_dep_finder.scan_exec_script(script_name)

def test_scan_exec_script_with_debug(mock_pkgutil, mock_strip_comments, ps_module_dep_finder):
    C.DEFAULT_DEBUG = True
    script_name = 'debug_script'
    mock_pkgutil.return_value = b'# Some comment\n$SomeCode = "Code"'

    # Call the method under test
    ps_module_dep_finder.scan_exec_script(script_name)

    # Assert that the script was added without stripping comments
    assert script_name in ps_module_dep_finder.exec_scripts
    assert ps_module_dep_finder.exec_scripts[script_name] == b'# Some comment\n$SomeCode = "Code"'

    # Reset the constant to its original value
    C.DEFAULT_DEBUG = False

def test_scan_exec_script_without_debug(mock_pkgutil, mock_strip_comments, ps_module_dep_finder):
    script_name = 'nodebug_script'
    mock_pkgutil.return_value = b'# Some comment\n$SomeCode = "Code"'
    mock_strip_comments.return_value = b'$SomeCode = "Code"'

    # Call the method under test
    ps_module_dep_finder.scan_exec_script(script_name)

    # Assert that the script was added with stripping comments
    assert script_name in ps_module_dep_finder.exec_scripts
    assert ps_module_dep_finder.exec_scripts[script_name] == b'$SomeCode = "Code"'
