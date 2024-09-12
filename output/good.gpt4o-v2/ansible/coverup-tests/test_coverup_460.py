# file: lib/ansible/modules/pip.py:352-360
# asked: {"lines": [352, 353, 354, 355, 356, 358, 359, 360], "branches": [[355, 356], [355, 358]]}
# gained: {"lines": [352, 353, 354, 355, 356, 358, 359, 360], "branches": [[355, 356], [355, 358]]}

import pytest
from unittest.mock import Mock

# Assuming _get_cmd_options is defined in the module under test
from ansible.modules.pip import _get_cmd_options

def test_get_cmd_options_success(monkeypatch):
    module = Mock()
    module.run_command = Mock(return_value=(0, "--option1 --option2", ""))
    
    result = _get_cmd_options(module, "dummy_cmd")
    
    module.run_command.assert_called_once_with("dummy_cmd --help")
    assert result == ["--option1", "--option2"]

def test_get_cmd_options_failure(monkeypatch):
    module = Mock()
    module.run_command = Mock(return_value=(1, "", "error"))
    module.fail_json = Mock(side_effect=Exception("Failed"))
    
    with pytest.raises(Exception, match="Failed"):
        _get_cmd_options(module, "dummy_cmd")
    
    module.run_command.assert_called_once_with("dummy_cmd --help")
    module.fail_json.assert_called_once_with(msg="Could not get output from dummy_cmd --help: error")
