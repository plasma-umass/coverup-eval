# file semantic_release/hvcs.py:429-439
# lines [429, 430, 435, 436, 437, 438, 439]
# branches []

import pytest
from semantic_release import ImproperConfigurationError
from semantic_release.hvcs import get_hvcs
from semantic_release.settings import config
from unittest.mock import patch

@pytest.fixture
def mock_config():
    with patch.object(config, 'get', return_value='invalid_hvcs') as mock:
        yield mock

def test_get_hvcs_invalid_option(mock_config):
    with pytest.raises(ImproperConfigurationError) as excinfo:
        get_hvcs()
    expected_message = '"invalid_hvcs" is not a valid option for hvcs.'
    actual_message = str(excinfo.value).format('invalid_hvcs')
    assert expected_message == actual_message
