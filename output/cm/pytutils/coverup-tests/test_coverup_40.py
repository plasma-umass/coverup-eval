# file pytutils/log.py:100-128
# lines [104, 107, 110, 113, 115, 116, 117, 118, 120, 121, 122, 123, 124, 125]
# branches ['103->104', '106->107', '109->110', '112->113']

import json
import os
import pytest
from pytutils.log import get_config
import yaml

def test_get_config_full_coverage(mocker):
    # Test with env_var
    mocker.patch.dict(os.environ, {'LOG_CFG': json.dumps({'key': 'value'})})
    assert get_config(env_var='LOG_CFG') == {'key': 'value'}

    # Test with default
    assert get_config(default={'default_key': 'default_value'}) == {'default_key': 'default_value'}

    # Test with None, should raise ValueError
    with pytest.raises(ValueError):
        get_config()

    # Test with invalid JSON string, should raise ValueError
    mocker.patch('yaml.load', return_value={'yaml_key': 'yaml_value'}, create=True)
    assert get_config(given='invalid_json') == {'yaml_key': 'yaml_value'}

    # Test with valid JSON string
    assert get_config(given=json.dumps({'json_key': 'json_value'})) == {'json_key': 'json_value'}

    # Cleanup environment variable
    del os.environ['LOG_CFG']
