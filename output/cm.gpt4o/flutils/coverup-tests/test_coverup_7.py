# file flutils/setuputils/cfg.py:25-29
# lines [25, 26, 27, 28, 29]
# branches []

import pytest
from flutils.setuputils.cfg import SetupCfgCommandConfig

def test_setup_cfg_command_config():
    # Create an instance of SetupCfgCommandConfig
    config = SetupCfgCommandConfig(
        name="test_name",
        camel="TestCamel",
        description="This is a test description",
        commands=("command1", "command2")
    )

    # Assertions to verify the postconditions
    assert config.name == "test_name"
    assert config.camel == "TestCamel"
    assert config.description == "This is a test description"
    assert config.commands == ("command1", "command2")

    # Clean up if necessary (not needed in this case as NamedTuple does not require cleanup)

