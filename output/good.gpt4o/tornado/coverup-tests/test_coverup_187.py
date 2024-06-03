# file tornado/util.py:309-310
# lines [309, 310]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the Configurable class is imported from tornado.util
from tornado.util import Configurable

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return cls

    @classmethod
    def configurable_default(cls):
        return cls

def test_configurable_initialize(mocker):
    # Create an instance of TestConfigurable
    configurable_instance = TestConfigurable()
    
    # Mock the _initialize method
    mock_initialize = mocker.patch.object(configurable_instance, '_initialize', wraps=configurable_instance._initialize)
    
    # Call the _initialize method
    configurable_instance._initialize()
    
    # Assert that the _initialize method was called once
    mock_initialize.assert_called_once()

    # Clean up by resetting the mock
    mock_initialize.reset_mock()
