# file httpie/config.py:74-79
# lines [79]
# branches ['78->79']

import pytest
import errno
from unittest import mock
from httpie.config import BaseConfigDict

@pytest.fixture
def base_config_dict():
    class MockPath:
        def __init__(self):
            self.parent = self

        def mkdir(self, mode=0o700, parents=True):
            pass

    return BaseConfigDict(path=MockPath())

def test_ensure_directory_oserror_not_eexist(base_config_dict):
    with mock.patch.object(base_config_dict.path.parent, 'mkdir', side_effect=OSError(errno.EACCES, "Permission denied")):
        with pytest.raises(OSError) as excinfo:
            base_config_dict.ensure_directory()
        assert excinfo.value.errno == errno.EACCES

def test_ensure_directory_oserror_eexist(base_config_dict):
    with mock.patch.object(base_config_dict.path.parent, 'mkdir', side_effect=OSError(errno.EEXIST, "File exists")):
        base_config_dict.ensure_directory()  # Should not raise an exception
