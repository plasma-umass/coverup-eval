# file httpie/config.py:61-62
# lines [61, 62]
# branches []

import pytest
from httpie.config import ConfigFileError

def test_config_file_error():
    with pytest.raises(ConfigFileError) as exc_info:
        raise ConfigFileError("An error occurred")
    assert str(exc_info.value) == "An error occurred"
