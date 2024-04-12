# file semantic_release/settings.py:64-74
# lines [64, 65, 66, 67, 68, 69, 70, 71, 72, 74]
# branches ['65->66', '65->74', '69->70', '69->74']

import os
import pytest
from semantic_release.settings import _config_from_pyproject
from unittest.mock import mock_open, patch
from tomlkit.exceptions import TOMLKitError

@pytest.fixture
def mock_pyproject(tmp_path):
    pyproject_path = tmp_path / "pyproject.toml"
    with open(pyproject_path, "w") as f:
        f.write('[tool.semantic_release]\nversion_variable = "src/__init__.py:__version__"')
    return str(pyproject_path)

@pytest.fixture
def mock_pyproject_bad_toml(tmp_path):
    pyproject_path = tmp_path / "pyproject.toml"
    with open(pyproject_path, "w") as f:
        f.write('tool.semantic_release]version_variable = "src/__init__.py:__version__"')
    return str(pyproject_path)

def test_config_from_pyproject_good_toml(mock_pyproject):
    config = _config_from_pyproject(mock_pyproject)
    assert config == {"version_variable": "src/__init__.py:__version__"}

def test_config_from_pyproject_bad_toml(mock_pyproject_bad_toml, caplog):
    with patch('semantic_release.settings.logger') as mock_logger:
        config = _config_from_pyproject(mock_pyproject_bad_toml)
        assert config == {}
        mock_logger.debug.assert_called_once()
        assert "Could not decode pyproject.toml" in mock_logger.debug.call_args[0][0]

def test_config_from_pyproject_nonexistent_file(tmp_path, caplog):
    non_existent_path = tmp_path / "nonexistent.toml"
    with patch('semantic_release.settings.logger') as mock_logger:
        config = _config_from_pyproject(str(non_existent_path))
        assert config == {}
        mock_logger.debug.assert_not_called()
