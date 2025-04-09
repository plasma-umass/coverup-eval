# file lib/ansible/cli/arguments/option_helpers.py:161-183
# lines [161, 163, 164, 166, 168, 169, 170, 171, 172, 173, 175, 176, 177, 178, 179, 180, 181, 182, 183]
# branches ['163->164', '163->166', '169->170', '169->171', '172->173', '172->175']

import pytest
from ansible.cli.arguments.option_helpers import version
from ansible import constants as C
import ansible
import sys

# Mocking the _gitinfo function and constants
@pytest.fixture
def mock_gitinfo(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers._gitinfo', return_value='gitinfo_stub')

@pytest.fixture
def mock_constants(mocker):
    mocker.patch.object(C, 'CONFIG_FILE', 'test_config_file')
    mocker.patch.object(C, 'DEFAULT_MODULE_PATH', 'test_module_path')
    mocker.patch.object(C, 'COLLECTIONS_PATHS', ['test_collection_path'])

@pytest.fixture
def mock_sys_argv(mocker):
    mocker.patch.object(sys, 'argv', ['test_executable'])

@pytest.fixture
def mock_jinja_version(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.j2_version', 'test_jinja_version')

@pytest.fixture
def mock_has_libyaml(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.HAS_LIBYAML', True)

# Test function to improve coverage
def test_version_with_prog(mock_gitinfo, mock_constants, mock_sys_argv, mock_jinja_version, mock_has_libyaml):
    prog = 'ansible-test'
    result = version(prog=prog)
    expected_result = "\n".join([
        f"{prog} [core {ansible.__version__}] gitinfo_stub",
        "  config file = test_config_file",
        "  configured module search path = test_module_path",
        f"  ansible python module location = {':'.join(ansible.__path__)}",
        "  ansible collection location = test_collection_path",
        "  executable location = test_executable",
        f"  python version = {''.join(sys.version.splitlines())}",
        "  jinja version = test_jinja_version",
        "  libyaml = True"
    ])
    assert result == expected_result

def test_version_without_prog(mock_gitinfo, mock_constants, mock_sys_argv, mock_jinja_version, mock_has_libyaml):
    result = version(prog=None)
    expected_result = "\n".join([
        f"{ansible.__version__} gitinfo_stub",
        "  config file = test_config_file",
        "  configured module search path = test_module_path",
        f"  ansible python module location = {':'.join(ansible.__path__)}",
        "  ansible collection location = test_collection_path",
        "  executable location = test_executable",
        f"  python version = {''.join(sys.version.splitlines())}",
        "  jinja version = test_jinja_version",
        "  libyaml = True"
    ])
    assert result == expected_result
