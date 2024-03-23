# file lib/ansible/module_utils/facts/network/dragonfly.py:23-28
# lines [23, 24, 28]
# branches []

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.facts.network.dragonfly import DragonFlyNetwork

# Since the DragonFlyNetwork class inherits from a class that requires a module argument,
# we need to mock the module argument for instantiation.

def test_dragonfly_network_instantiation(mocker):
    mock_module = MagicMock()
    dragonfly_network = DragonFlyNetwork(module=mock_module)
    assert dragonfly_network.platform == 'DragonFly'
