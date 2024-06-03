# file lib/ansible/cli/arguments/option_helpers.py:161-183
# lines [173]
# branches ['169->171', '172->173']

import pytest
from unittest import mock
from ansible.cli.arguments.option_helpers import version

@pytest.fixture
def mock_constants(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.C.CONFIG_FILE', 'test_config_file')
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_MODULE_PATH', None)
    mocker.patch('ansible.cli.arguments.option_helpers.C.COLLECTIONS_PATHS', ['test_collection_path'])
    mocker.patch('ansible.cli.arguments.option_helpers.__version__', '2.9.10')
    mocker.patch('ansible.cli.arguments.option_helpers.ansible.__path__', ['test_ansible_path'])
    mocker.patch('ansible.cli.arguments.option_helpers.j2_version', '2.11.3')
    mocker.patch('ansible.cli.arguments.option_helpers.HAS_LIBYAML', True)
    mocker.patch('ansible.cli.arguments.option_helpers.sys.argv', ['test_executable'])
    mocker.patch('ansible.cli.arguments.option_helpers.sys.version', '3.8.5')

def test_version_with_gitinfo(mock_constants, mocker):
    mocker.patch('ansible.cli.arguments.option_helpers._gitinfo', return_value='test_git_info')
    result = version('ansible')
    assert "ansible [core 2.9.10] test_git_info" in result
    assert "  config file = test_config_file" in result
    assert "  configured module search path = Default w/o overrides" in result
    assert "  ansible python module location = test_ansible_path" in result
    assert "  ansible collection location = test_collection_path" in result
    assert "  executable location = test_executable" in result
    assert "  python version = 3.8.5" in result
    assert "  jinja version = 2.11.3" in result
    assert "  libyaml = True" in result

def test_version_without_gitinfo(mock_constants, mocker):
    mocker.patch('ansible.cli.arguments.option_helpers._gitinfo', return_value=None)
    result = version('ansible')
    assert "ansible [core 2.9.10]" in result
    assert "  config file = test_config_file" in result
    assert "  configured module search path = Default w/o overrides" in result
    assert "  ansible python module location = test_ansible_path" in result
    assert "  ansible collection location = test_collection_path" in result
    assert "  executable location = test_executable" in result
    assert "  python version = 3.8.5" in result
    assert "  jinja version = 2.11.3" in result
    assert "  libyaml = True" in result
