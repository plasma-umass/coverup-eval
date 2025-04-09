# file lib/ansible/cli/arguments/option_helpers.py:161-183
# lines [161, 163, 164, 166, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183]
# branches ['163->164', '163->166', '169->170', '169->171', '172->173', '172->175']

import pytest
from unittest import mock
import sys
import ansible
from ansible.cli.arguments.option_helpers import version

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.C.CONFIG_FILE', 'test_config_file')
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_MODULE_PATH', 'test_module_path')
    mocker.patch('ansible.cli.arguments.option_helpers.C.COLLECTIONS_PATHS', ['test_collection_path'])
    mocker.patch('ansible.cli.arguments.option_helpers.__version__', '2.9.10')
    mocker.patch('ansible.cli.arguments.option_helpers.j2_version', '2.11.3')
    mocker.patch('ansible.cli.arguments.option_helpers.HAS_LIBYAML', True)
    mocker.patch('ansible.cli.arguments.option_helpers._gitinfo', return_value='test_git_info')

def test_version_with_prog(mock_constants):
    result = version(prog='ansible')
    assert "ansible [core 2.9.10] test_git_info" in result
    assert "config file = test_config_file" in result
    assert "configured module search path = test_module_path" in result
    assert "ansible python module location = " in result
    assert "ansible collection location = test_collection_path" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = 2.11.3" in result
    assert "libyaml = True" in result

def test_version_without_prog(mock_constants):
    result = version()
    assert "2.9.10 test_git_info" in result
    assert "config file = test_config_file" in result
    assert "configured module search path = test_module_path" in result
    assert "ansible python module location = " in result
    assert "ansible collection location = test_collection_path" in result
    assert "executable location = " in result
    assert "python version = " in result
    assert "jinja version = 2.11.3" in result
    assert "libyaml = True" in result
