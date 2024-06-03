# file semantic_release/pypi.py:17-70
# lines [17, 18, 19, 33, 34, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 64, 65, 68, 70]
# branches ['33->34', '33->37', '40->42', '40->51', '45->48', '45->57', '51->52', '51->54']

import os
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.pypi import upload_to_pypi, ImproperConfigurationError

def test_upload_to_pypi_with_token(mocker):
    mocker.patch.dict(os.environ, {"PYPI_TOKEN": "pypi-12345"})
    mock_run = mocker.patch("semantic_release.pypi.run")

    upload_to_pypi()

    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-12345' \"dist/*\"")

def test_upload_to_pypi_with_username_password(mocker):
    mocker.patch.dict(os.environ, {"PYPI_USERNAME": "user", "PYPI_PASSWORD": "pass"})
    mock_run = mocker.patch("semantic_release.pypi.run")

    upload_to_pypi()

    mock_run.assert_called_once_with("twine upload -u 'user' -p 'pass' \"dist/*\"")

def test_upload_to_pypi_missing_credentials(mocker):
    mocker.patch.dict(os.environ, {}, clear=True)
    mocker.patch("os.path.isfile", return_value=False)

    with pytest.raises(ImproperConfigurationError, match="Missing credentials for uploading to PyPI"):
        upload_to_pypi()

def test_upload_to_pypi_invalid_token(mocker):
    mocker.patch.dict(os.environ, {"PYPI_TOKEN": "invalid-token"})
    
    with pytest.raises(ImproperConfigurationError, match='PyPI token should begin with "pypi-"'):
        upload_to_pypi()

def test_upload_to_pypi_with_repository(mocker):
    mocker.patch.dict(os.environ, {"PYPI_TOKEN": "pypi-12345"})
    mocker.patch("semantic_release.pypi.config.get", return_value="https://test.pypi.org/legacy/")
    mock_run = mocker.patch("semantic_release.pypi.run")

    upload_to_pypi()

    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-12345' -r 'https://test.pypi.org/legacy/' \"dist/*\"")

def test_upload_to_pypi_with_skip_existing(mocker):
    mocker.patch.dict(os.environ, {"PYPI_TOKEN": "pypi-12345"})
    mock_run = mocker.patch("semantic_release.pypi.run")

    upload_to_pypi(skip_existing=True)

    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-12345' --skip-existing \"dist/*\"")

def test_upload_to_pypi_with_glob_patterns(mocker):
    mocker.patch.dict(os.environ, {"PYPI_TOKEN": "pypi-12345"})
    mock_run = mocker.patch("semantic_release.pypi.run")

    upload_to_pypi(glob_patterns=["*.whl", "*.tar.gz"])

    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-12345' \"dist/*.whl\" \"dist/*.tar.gz\"")
