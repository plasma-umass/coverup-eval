# file isort/exceptions.py:63-71
# lines [63, 64, 66, 67, 68, 70]
# branches []

import pytest
from isort.exceptions import FileSkipSetting

def test_file_skip_setting_exception():
    file_path = "test_file.py"
    exception = FileSkipSetting(file_path)
    
    assert str(exception) == f"{file_path} was skipped as it's listed in 'skip' setting or matches a glob in 'skip_glob' setting"
    assert exception.file_path == file_path
