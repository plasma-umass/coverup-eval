# file: semantic_release/hvcs.py:484-490
# asked: {"lines": [484, 490], "branches": []}
# gained: {"lines": [484, 490], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import get_token, get_hvcs
from semantic_release.errors import ImproperConfigurationError

@pytest.fixture
def mock_hvcs(monkeypatch):
    mock_hvcs_class = MagicMock()
    mock_hvcs_class.token.return_value = "fake_token"
    monkeypatch.setattr("semantic_release.hvcs.get_hvcs", lambda: mock_hvcs_class)
    return mock_hvcs_class

def test_get_token_success(mock_hvcs):
    token = get_token()
    assert token == "fake_token"
    mock_hvcs.token.assert_called_once()

def test_get_token_improper_configuration(monkeypatch):
    monkeypatch.setattr("semantic_release.hvcs.config.get", lambda _: "invalid_hvcs")
    with pytest.raises(ImproperConfigurationError):
        get_hvcs()
