# file: httpie/config.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from pathlib import Path
from httpie.config import BaseConfigDict

def test_baseconfigdict_init():
    # Create a temporary path object
    temp_path = Path('/tmp/test_config')

    # Initialize BaseConfigDict with the temporary path
    config = BaseConfigDict(temp_path)

    # Assert that the path attribute is set correctly
    assert config.path == temp_path

    # Clean up if necessary (e.g., remove temporary files or directories)
    # In this case, there's no actual file creation, so no cleanup is needed.
