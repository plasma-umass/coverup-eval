# file lib/ansible/executor/powershell/module_manifest.py:286-402
# lines [286, 296, 297, 300, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 313, 315, 316, 317, 318, 320, 321, 322, 323, 324, 326, 327, 328, 330, 331, 332, 333, 335, 336, 337, 338, 339, 341, 342, 343, 344, 346, 347, 348, 349, 351, 352, 353, 354, 356, 357, 360, 361, 362, 367, 368, 370, 372, 373, 374, 376, 377, 378, 380, 381, 382, 383, 385, 386, 387, 388, 390, 391, 392, 393, 396, 397, 399, 401, 402]
# branches ['297->300', '297->302', '315->316', '315->326', '326->327', '326->335', '337->338', '337->346', '352->353', '352->360', '360->361', '360->367', '373->374', '373->376', '376->377', '376->380', '380->381', '380->385', '386->387', '386->390', '387->386', '387->388', '390->391', '390->393', '396->397', '396->399']

import pytest
import base64
import json
import random
from unittest.mock import MagicMock, patch
from ansible.executor.powershell.module_manifest import _create_powershell_wrapper

@pytest.fixture
def mock_psmoduledfinder(mocker):
    mock_finder = mocker.patch('ansible.executor.powershell.module_manifest.PSModuleDepFinder', autospec=True)
    instance = mock_finder.return_value
    instance.ps_version = '5.1'
    instance.os_version = '10.0'
    instance.exec_scripts = {}
    instance.ps_modules = {}
    instance.cs_utils_wrapper = {}
    instance.cs_utils_module = {}
    instance.become = False
    instance.scan_exec_script.side_effect = lambda script: instance.exec_scripts.setdefault(script, b"")
    return instance

@pytest.fixture
def mock_config(mocker):
    mock_C = mocker.patch('ansible.executor.powershell.module_manifest.C', autospec=True)
    mock_C.config.get_config_value.side_effect = lambda key, variables=None: {
        'WIN_ASYNC_STARTUP_TIMEOUT': 30,
        'COVERAGE_REMOTE_OUTPUT': 'coverage_output_path',
        'COVERAGE_REMOTE_PATHS': 'coverage_remote_paths'
    }.get(key, None)
    return mock_C

def test_create_powershell_wrapper(mock_psmoduledfinder, mock_config):
    b_module_data = b"test_module_data"
    module_path = "test_module_path"
    module_args = ["arg1", "arg2"]
    environment = {"env1": "value1"}
    async_timeout = 10
    become = True
    become_method = "runas"
    become_user = "test_user"
    become_password = "test_password"
    become_flags = ["flag1"]
    substyle = "powershell"
    task_vars = {"var1": "value1"}
    module_fqn = "test.module.fqn"

    result = _create_powershell_wrapper(
        b_module_data, module_path, module_args, environment, async_timeout, become,
        become_method, become_user, become_password, become_flags, substyle, task_vars, module_fqn
    )

    assert result is not None
    assert isinstance(result, bytes)
    assert b'\0\0\0\0' in result

    exec_manifest = json.loads(result.split(b'\0\0\0\0')[1].decode('utf-8'))
    assert exec_manifest['module_entry'] == base64.b64encode(b_module_data).decode('utf-8')
    assert exec_manifest['module_args'] == module_args
    assert exec_manifest['environment'] == environment
    assert exec_manifest['async_jid'] is not None
    assert exec_manifest['async_timeout_sec'] == async_timeout
    assert exec_manifest['async_startup_timeout'] == 30
    assert exec_manifest['become_user'] == become_user
    assert exec_manifest['become_password'] == become_password
    assert exec_manifest['become_flags'] == become_flags
    assert exec_manifest['min_ps_version'] == '5.1'
    assert exec_manifest['min_os_version'] == '10.0'
    assert 'coverage' in exec_manifest
    assert exec_manifest['coverage']['output'] == 'coverage_output_path'
    assert exec_manifest['coverage']['path_filter'] == 'coverage_remote_paths'
