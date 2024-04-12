# file httpie/config.py:81-82
# lines [81, 82]
# branches []

import pytest
from httpie.config import BaseConfigDict
from pathlib import Path

class TestableBaseConfigDict(BaseConfigDict):
    def __init__(self, *args, **kwargs):
        if 'path' not in kwargs:
            kwargs['path'] = Path()
        super().__init__(*args, **kwargs)

def test_base_config_dict_is_new(tmp_path):
    # Create a temporary file to represent the config file
    temp_config_file = tmp_path / "config.json"
    
    # Instantiate TestableBaseConfigDict with a mocked 'path' attribute
    config_dict = TestableBaseConfigDict(path=temp_config_file)
    
    # Test the is_new method before the file exists
    assert config_dict.is_new() == True, "is_new should return True when the file does not exist"
    
    # Create the file and test the is_new method again
    temp_config_file.touch()
    assert config_dict.is_new() == False, "is_new should return False when the file exists"
    
    # No need to clean up: the temporary directory is handled by pytest
