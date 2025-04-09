# file: httpie/config.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from httpie.config import ConfigFileError

def test_config_file_error():
    with pytest.raises(ConfigFileError):
        raise ConfigFileError("This is a test error")

