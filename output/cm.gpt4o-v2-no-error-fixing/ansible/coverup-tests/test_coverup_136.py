# file: lib/ansible/config/manager.py:171-183
# asked: {"lines": [171, 173, 174, 175, 176, 177, 178, 179, 181, 183], "branches": [[174, 175], [174, 183], [176, 177], [176, 178], [178, 179], [178, 181]]}
# gained: {"lines": [171, 173, 174, 175, 176, 177, 178, 179, 181, 183], "branches": [[174, 175], [174, 183], [176, 177], [176, 178], [178, 179], [178, 181]]}

import os
import pytest
from ansible.errors import AnsibleOptionsError
from ansible.module_utils._text import to_native
from ansible.config.manager import get_config_type

def test_get_config_type_ini():
    assert get_config_type('config.ini') == 'ini'

def test_get_config_type_cfg():
    assert get_config_type('config.cfg') == 'ini'

def test_get_config_type_yaml():
    assert get_config_type('config.yaml') == 'yaml'

def test_get_config_type_yml():
    assert get_config_type('config.yml') == 'yaml'

def test_get_config_type_unsupported():
    with pytest.raises(AnsibleOptionsError, match="Unsupported configuration file extension for config.txt: .txt"):
        get_config_type('config.txt')

def test_get_config_type_none():
    assert get_config_type(None) is None
