# file semantic_release/pypi.py:17-70
# lines [17, 18, 19, 33, 34, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 64, 65, 68, 70]
# branches ['33->34', '33->37', '40->42', '40->51', '45->48', '45->57', '51->52', '51->54']

import os
from unittest.mock import patch
import pytest
from semantic_release.pypi import upload_to_pypi
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_environment(monkeypatch):
    monkeypatch.setenv("HOME", "/nonexistent")
    yield
    monkeypatch.undo()

@pytest.fixture
def mock_run(mocker):
    return mocker.patch('semantic_release.pypi.run')

def test_upload_to_pypi_without_credentials(mock_environment, mock_run):
    with pytest.raises(ImproperConfigurationError) as excinfo:
        upload_to_pypi()
    assert "Missing credentials for uploading to PyPI" in str(excinfo.value)
    mock_run.assert_not_called()

def test_upload_to_pypi_with_invalid_token(mock_environment, mock_run):
    with patch.dict(os.environ, {"PYPI_TOKEN": "invalid-token"}):
        with pytest.raises(ImproperConfigurationError) as excinfo:
            upload_to_pypi()
    assert 'PyPI token should begin with "pypi-"' in str(excinfo.value)
    mock_run.assert_not_called()

def test_upload_to_pypi_with_valid_token(mock_environment, mock_run):
    with patch.dict(os.environ, {"PYPI_TOKEN": "pypi-validtoken"}):
        upload_to_pypi()
    mock_run.assert_called_once()
    assert "__token__" in mock_run.call_args[0][0]
    assert "pypi-validtoken" in mock_run.call_args[0][0]

def test_upload_to_pypi_with_username_password(mock_environment, mock_run):
    with patch.dict(os.environ, {"PYPI_USERNAME": "user", "PYPI_PASSWORD": "pass"}):
        upload_to_pypi()
    mock_run.assert_called_once()
    assert "-u 'user' -p 'pass'" in mock_run.call_args[0][0]

def test_upload_to_pypi_with_skip_existing(mock_environment, mock_run):
    with patch.dict(os.environ, {"PYPI_USERNAME": "user", "PYPI_PASSWORD": "pass"}):
        upload_to_pypi(skip_existing=True)
    mock_run.assert_called_once()
    assert "--skip-existing" in mock_run.call_args[0][0]

def test_upload_to_pypi_with_custom_glob_patterns(mock_environment, mock_run):
    with patch.dict(os.environ, {"PYPI_USERNAME": "user", "PYPI_PASSWORD": "pass"}):
        upload_to_pypi(glob_patterns=["*.whl"])
    mock_run.assert_called_once()
    assert '"dist/*.whl"' in mock_run.call_args[0][0]

def test_upload_to_pypi_with_repository(mock_environment, mock_run):
    with patch.dict(os.environ, {"PYPI_USERNAME": "user", "PYPI_PASSWORD": "pass"}):
        with patch('semantic_release.pypi.config.get', return_value='test_repo'):
            upload_to_pypi()
    mock_run.assert_called_once()
    assert "-r 'test_repo'" in mock_run.call_args[0][0]
