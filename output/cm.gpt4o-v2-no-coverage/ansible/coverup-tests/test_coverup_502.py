# file: lib/ansible/modules/pip.py:352-360
# asked: {"lines": [352, 353, 354, 355, 356, 358, 359, 360], "branches": [[355, 356], [355, 358]]}
# gained: {"lines": [352, 353, 354, 355, 356, 358, 359, 360], "branches": [[355, 356], [355, 358]]}

import pytest

class MockModule:
    def run_command(self, cmd):
        if cmd == "pip --help":
            return (0, "--option1 --option2", "")
        elif cmd == "failcmd --help":
            return (1, "", "error")
        return (0, "", "")

    def fail_json(self, msg):
        raise Exception(msg)

from ansible.modules.pip import _get_cmd_options

def test_get_cmd_options_success():
    module = MockModule()
    cmd = "pip"
    result = _get_cmd_options(module, cmd)
    assert result == ["--option1", "--option2"]

def test_get_cmd_options_failure():
    module = MockModule()
    cmd = "failcmd"
    with pytest.raises(Exception) as excinfo:
        _get_cmd_options(module, cmd)
    assert "Could not get output from failcmd --help: error" in str(excinfo.value)
