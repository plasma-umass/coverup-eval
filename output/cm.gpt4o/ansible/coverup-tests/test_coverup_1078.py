# file lib/ansible/executor/powershell/module_manifest.py:286-402
# lines [338, 339, 341, 342, 343, 344, 361, 362, 374, 381, 382, 383, 388, 391, 392]
# branches ['297->302', '315->326', '326->335', '337->338', '352->360', '360->361', '373->374', '380->381', '387->388', '390->391', '396->399']

import pytest
from unittest.mock import patch, MagicMock
from ansible.executor.powershell.module_manifest import _create_powershell_wrapper, PSModuleDepFinder, C, to_text, to_bytes
import base64
import json
import random

@pytest.fixture
def mock_finder(mocker):
    mock_finder = mocker.patch('ansible.executor.powershell.module_manifest.PSModuleDepFinder', autospec=True)
    instance = mock_finder.return_value
    instance.ps_version = '5.1'
    instance.os_version = '10.0.17763.0'
    instance.become = True
    instance.exec_scripts = {'exec_wrapper': b''}
    instance.ps_modules = {}
    instance.cs_utils_wrapper = {}
    instance.cs_utils_module = {}
    return instance

@pytest.fixture
def mock_config(mocker):
    mock_config = mocker.patch('ansible.executor.powershell.module_manifest.C.config.get_config_value', autospec=True)
    mock_config.side_effect = lambda key, variables=None: {
        'WIN_ASYNC_STARTUP_TIMEOUT': 30,
        'COVERAGE_REMOTE_OUTPUT': 'coverage_output_path',
        'COVERAGE_REMOTE_PATHS': 'coverage_paths'
    }.get(key, None)
    return mock_config

def test_create_powershell_wrapper_full_coverage(mock_finder, mock_config):
    b_module_data = b"test_module_data"
    module_path = "test_module_path"
    module_args = ["arg1", "arg2"]
    environment = {"env1": "value1"}
    async_timeout = 10
    become = True
    become_method = "runas"
    become_user = "test_user"
    become_password = "test_password"
    become_flags = "test_flags"
    substyle = "powershell"
    task_vars = {}
    module_fqn = "test_module_fqn"

    result = _create_powershell_wrapper(
        b_module_data, module_path, module_args, environment, async_timeout, become,
        become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn
    )

    assert result is not None
    assert b'\0\0\0\0' in result

    exec_manifest = json.loads(result.split(b'\0\0\0\0')[1].decode('utf-8'))
    assert exec_manifest['module_entry'] == to_text(base64.b64encode(b_module_data))
    assert 'become_wrapper' in exec_manifest['actions']
    assert exec_manifest['become_user'] == become_user
    assert exec_manifest['become_password'] == become_password
    assert exec_manifest['become_flags'] == become_flags
    assert exec_manifest['async_timeout_sec'] == async_timeout
    assert exec_manifest['async_startup_timeout'] == 30
    if 'coverage_wrapper' in exec_manifest:
        assert exec_manifest['coverage'] is not None
    assert exec_manifest['powershell_modules'] == {}
    assert exec_manifest['csharp_utils'] == {}
    assert exec_manifest['csharp_utils_module'] == []
