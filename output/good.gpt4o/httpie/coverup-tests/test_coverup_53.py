# file httpie/config.py:70-72
# lines [70, 71, 72]
# branches []

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

def test_base_config_dict_initialization():
    # Create a temporary path object
    temp_path = Path('/tmp/test_config.json')
    
    # Initialize the BaseConfigDict with the temporary path
    config_dict = BaseConfigDict(temp_path)
    
    # Assert that the path is correctly set
    assert config_dict.path == temp_path
    
    # Assert that the dictionary is initialized empty
    assert len(config_dict) == 0
