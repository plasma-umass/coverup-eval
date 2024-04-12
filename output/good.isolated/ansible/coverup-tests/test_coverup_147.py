# file lib/ansible/config/manager.py:316-341
# lines [316, 320, 321, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 341]
# branches ['320->321', '320->323', '324->exit', '324->325', '325->326', '325->341']

import pytest
from ansible.config.manager import ConfigManager
from ansible.errors import AnsibleOptionsError
from ansible.module_utils._text import to_bytes, to_text, to_native
import configparser
import os
import tempfile

# Mock function to replace get_config_type
def mock_get_config_type(cfile):
    return 'ini'

# Test function to improve coverage
def test_parse_config_file_ini(mocker):
    # Setup temporary config file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(b"[defaults]\nexample = value")
        tmp_path = tmp.name

    # Mock the get_config_type function to return 'ini'
    mocker.patch('ansible.config.manager.get_config_type', side_effect=mock_get_config_type)

    # Create ConfigManager instance and call _parse_config_file
    cm = ConfigManager()
    cm._parsers = {}
    cm._parse_config_file(cfile=tmp_path)

    # Check if the parser for the file was created and contains the correct data
    assert tmp_path in cm._parsers
    assert cm._parsers[tmp_path].get('defaults', 'example') == 'value'

    # Clean up temporary file
    os.unlink(tmp_path)

# Test function to handle unsupported file type
def test_parse_config_file_unsupported(mocker):
    # Setup temporary config file
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp_path = tmp.name

    # Mock the get_config_type function to return an unsupported type
    mocker.patch('ansible.config.manager.get_config_type', return_value='unsupported')

    # Create ConfigManager instance and call _parse_config_file expecting an error
    cm = ConfigManager()
    cm._parsers = {}
    with pytest.raises(AnsibleOptionsError) as excinfo:
        cm._parse_config_file(cfile=tmp_path)

    # Check if the error message is correct
    assert "Unsupported configuration file type" in str(excinfo.value)

    # Clean up temporary file
    os.unlink(tmp_path)
