# file semantic_release/settings.py:121-135
# lines [121, 126, 127, 128, 129, 130, 131, 132, 133, 135]
# branches ['128->129', '128->133', '129->130', '129->133', '131->129', '131->132']

import pytest
from unittest.mock import patch
from semantic_release.settings import overload_configuration

# Mock configuration dictionary
config = {}

@overload_configuration
def dummy_function(*args, **kwargs):
    return "Function executed"

def test_overload_configuration(mocker):
    global config
    mock_config = mocker.patch.dict('semantic_release.settings.config', {}, clear=True)

    # Test with define parameter
    result = dummy_function(define=["key1=value1", "key2=value2"])
    assert mock_config["key1"] == "value1"
    assert mock_config["key2"] == "value2"
    assert result == "Function executed"

    # Test without define parameter
    mock_config.clear()
    result = dummy_function()
    assert mock_config == {}
    assert result == "Function executed"

    # Test with invalid define parameter
    mock_config.clear()
    result = dummy_function(define=["key1value1", "key2=value2"])
    assert "key1" not in mock_config
    assert mock_config["key2"] == "value2"
    assert result == "Function executed"
