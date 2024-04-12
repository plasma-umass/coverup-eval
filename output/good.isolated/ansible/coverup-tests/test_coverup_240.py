# file lib/ansible/config/manager.py:171-183
# lines [171, 173, 174, 175, 176, 177, 178, 179, 181, 183]
# branches ['174->175', '174->183', '176->177', '176->178', '178->179', '178->181']

import os
import pytest
from ansible.errors import AnsibleOptionsError
from ansible.config.manager import get_config_type

# Assuming the function get_config_type is part of a module named ansible.config.manager
# and that AnsibleOptionsError is the correct exception to be raised for this case.

def test_get_config_type_ini(tmp_path, mocker):
    ini_file = tmp_path / "config.ini"
    ini_file.touch()
    assert get_config_type(str(ini_file)) == 'ini'

def test_get_config_type_yaml(tmp_path, mocker):
    yaml_file = tmp_path / "config.yaml"
    yaml_file.touch()
    assert get_config_type(str(yaml_file)) == 'yaml'

def test_get_config_type_unsupported_extension(tmp_path, mocker):
    unsupported_file = tmp_path / "config.unsupported"
    unsupported_file.touch()
    with pytest.raises(AnsibleOptionsError):
        get_config_type(str(unsupported_file))

def test_get_config_type_none():
    assert get_config_type(None) is None
