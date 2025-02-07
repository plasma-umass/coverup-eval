# file: semantic_release/settings.py:121-135
# asked: {"lines": [126, 127, 128, 129, 130, 131, 132, 133, 135], "branches": [[128, 129], [128, 133], [129, 130], [129, 133], [131, 129], [131, 132]]}
# gained: {"lines": [126, 127, 128, 129, 130, 131, 132, 133, 135], "branches": [[128, 129], [128, 133], [129, 130], [129, 133], [131, 129], [131, 132]]}

import pytest
from functools import wraps

# Import the function to be tested
from semantic_release.settings import overload_configuration

@pytest.fixture
def config(monkeypatch):
    config = {}
    monkeypatch.setattr('semantic_release.settings.config', config)
    return config

def test_overload_configuration_with_define(config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        return True

    # Test case where 'define' is in kwargs and has valid key=value pairs
    result = dummy_function(define=["key1=value1", "key2=value2"])
    assert result is True
    assert config["key1"] == "value1"
    assert config["key2"] == "value2"

def test_overload_configuration_without_define(config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        return True

    # Test case where 'define' is not in kwargs
    result = dummy_function()
    assert result is True
    assert config == {}

def test_overload_configuration_with_invalid_define(config):
    @overload_configuration
    def dummy_function(*args, **kwargs):
        return True

    # Test case where 'define' has an invalid key=value pair
    result = dummy_function(define=["key1=value1", "invalidpair"])
    assert result is True
    assert config["key1"] == "value1"
    assert "invalidpair" not in config
