# file: flutils/setuputils/cfg.py:25-29
# asked: {"lines": [25, 26, 27, 28, 29], "branches": []}
# gained: {"lines": [25, 26, 27, 28, 29], "branches": []}

import pytest
from flutils.setuputils.cfg import SetupCfgCommandConfig

def test_setup_cfg_command_config():
    config = SetupCfgCommandConfig(
        name="test_name",
        camel="TestName",
        description="This is a test description.",
        commands=("command1", "command2")
    )
    
    assert config.name == "test_name"
    assert config.camel == "TestName"
    assert config.description == "This is a test description."
    assert config.commands == ("command1", "command2")
