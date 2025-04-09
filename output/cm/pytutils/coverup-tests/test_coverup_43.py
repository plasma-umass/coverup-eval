# file pytutils/log.py:100-128
# lines [122, 123, 124, 125]
# branches []

import os
import pytest
from unittest.mock import patch
from pytutils.log import get_config

def test_get_config_invalid_yaml(mocker):
    invalid_yaml = "unparseable: {"
    mocker.patch('os.environ.get', return_value=invalid_yaml)
    mocker.patch('yaml.load', side_effect=ValueError("mocked error"))
    with pytest.raises(ValueError) as excinfo:
        get_config(env_var='LOG_CFG')
    assert "Could not parse logging config as bare, json, or yaml" in str(excinfo.value)
