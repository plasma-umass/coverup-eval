# file thefuck/entrypoints/not_configured.py:82-88
# lines [84, 85, 86, 87, 88]
# branches []

import pytest
from thefuck.entrypoints.not_configured import _configure
from pathlib import Path
from unittest.mock import Mock

@pytest.fixture
def mock_configuration_details(tmp_path):
    config_file = tmp_path / "shell_config"
    config_content = "alias fuck='eval $(thefuck $(fc -ln -1))'"
    return Mock(path=str(config_file), content=config_content)

def test_configure_writes_to_file(mock_configuration_details):
    # Arrange
    expected_content = "\n{}\n".format(mock_configuration_details.content)

    # Act
    _configure(mock_configuration_details)

    # Assert
    with open(mock_configuration_details.path, 'r') as f:
        content = f.read()
    assert content == expected_content
