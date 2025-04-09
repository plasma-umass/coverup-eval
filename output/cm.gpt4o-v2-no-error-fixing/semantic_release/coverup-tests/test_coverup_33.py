# file: semantic_release/pypi.py:17-70
# asked: {"lines": [17, 18, 19, 33, 34, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 64, 65, 68, 70], "branches": [[33, 34], [33, 37], [40, 42], [40, 51], [45, 48], [45, 57], [51, 52], [51, 54]]}
# gained: {"lines": [17, 18, 19, 33, 34, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 51, 52, 54, 55, 57, 58, 60, 61, 64, 65, 68, 70], "branches": [[33, 34], [33, 37], [40, 42], [40, 51], [45, 48], [45, 57], [51, 52], [51, 54]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.pypi import upload_to_pypi
from semantic_release import ImproperConfigurationError

@pytest.fixture
def mock_run():
    with patch('semantic_release.pypi.run') as mock:
        yield mock

def test_upload_to_pypi_with_token(monkeypatch, mock_run):
    monkeypatch.setenv('PYPI_TOKEN', 'pypi-valid-token')
    upload_to_pypi()
    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-valid-token' \"dist/*\"")

def test_upload_to_pypi_with_username_password(monkeypatch, mock_run):
    monkeypatch.setenv('PYPI_USERNAME', 'username')
    monkeypatch.setenv('PYPI_PASSWORD', 'password')
    upload_to_pypi()
    mock_run.assert_called_once_with("twine upload -u 'username' -p 'password' \"dist/*\"")

def test_upload_to_pypi_missing_credentials(monkeypatch):
    monkeypatch.delenv('PYPI_TOKEN', raising=False)
    monkeypatch.delenv('PYPI_USERNAME', raising=False)
    monkeypatch.delenv('PYPI_PASSWORD', raising=False)
    monkeypatch.setattr(os.path, 'isfile', lambda x: False)
    with pytest.raises(ImproperConfigurationError, match="Missing credentials for uploading to PyPI"):
        upload_to_pypi()

def test_upload_to_pypi_invalid_token(monkeypatch):
    monkeypatch.setenv('PYPI_TOKEN', 'invalid-token')
    with pytest.raises(ImproperConfigurationError, match='PyPI token should begin with "pypi-"'):
        upload_to_pypi()

def test_upload_to_pypi_with_repository(monkeypatch, mock_run):
    monkeypatch.setenv('PYPI_TOKEN', 'pypi-valid-token')
    monkeypatch.setattr('semantic_release.settings.config.get', lambda key, default=None: 'https://test.pypi.org/legacy/' if key == 'repository' else default)
    upload_to_pypi()
    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-valid-token' -r 'https://test.pypi.org/legacy/' \"dist/*\"")

def test_upload_to_pypi_with_skip_existing(monkeypatch, mock_run):
    monkeypatch.setenv('PYPI_TOKEN', 'pypi-valid-token')
    upload_to_pypi(skip_existing=True)
    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-valid-token' --skip-existing \"dist/*\"")

def test_upload_to_pypi_with_glob_patterns(monkeypatch, mock_run):
    monkeypatch.setenv('PYPI_TOKEN', 'pypi-valid-token')
    upload_to_pypi(glob_patterns=['*.whl', '*.tar.gz'])
    mock_run.assert_called_once_with("twine upload -u '__token__' -p 'pypi-valid-token' \"dist/*.whl\" \"dist/*.tar.gz\"")
