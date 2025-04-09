# file: lib/ansible/modules/apt_repository.py:506-513
# asked: {"lines": [506, 507, 508, 510, 511, 513], "branches": [[510, 511], [510, 513]]}
# gained: {"lines": [506, 507, 508, 510, 511, 513], "branches": [[510, 511], [510, 513]]}

import pytest
from unittest.mock import Mock
from ansible.modules.apt_repository import get_add_ppa_signing_key_callback

def test_get_add_ppa_signing_key_callback_check_mode():
    module = Mock()
    module.check_mode = True

    result = get_add_ppa_signing_key_callback(module)
    
    assert result is None

def test_get_add_ppa_signing_key_callback_run_command():
    module = Mock()
    module.check_mode = False
    module.run_command = Mock()

    result = get_add_ppa_signing_key_callback(module)
    
    assert result is not None
    command = "dummy_command"
    result(command)
    module.run_command.assert_called_once_with(command, check_rc=True)
