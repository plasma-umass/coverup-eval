# file: lib/ansible/galaxy/token.py:112-121
# asked: {"lines": [112, 113, 114, 115, 118, 119, 121], "branches": [[114, 115], [114, 118], [118, 119], [118, 121]]}
# gained: {"lines": [112, 113, 114, 115, 118, 119, 121], "branches": [[114, 115], [118, 119], [118, 121]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.galaxy.token import GalaxyToken, NoTokenSentinel

@pytest.fixture
def mock_config_file(tmp_path):
    config_file = tmp_path / "mock_galaxy_token.yml"
    config_file.write_text("")
    return config_file

def test_galaxy_token_config_with_no_token(mock_config_file, monkeypatch):
    monkeypatch.setattr("ansible.galaxy.token.C.GALAXY_TOKEN_PATH", str(mock_config_file))
    token = GalaxyToken()
    
    with patch("ansible.galaxy.token.open", mock_open(read_data="{}")), \
         patch("ansible.galaxy.token.os.path.isfile", return_value=True), \
         patch("ansible.galaxy.token.yaml_load", return_value={}):
        config = token.config
    
    assert config == {}

def test_galaxy_token_config_with_token(mock_config_file, monkeypatch):
    monkeypatch.setattr("ansible.galaxy.token.C.GALAXY_TOKEN_PATH", str(mock_config_file))
    token_value = "test_token"
    token = GalaxyToken(token=token_value)
    
    with patch("ansible.galaxy.token.open", mock_open(read_data="{}")), \
         patch("ansible.galaxy.token.os.path.isfile", return_value=True), \
         patch("ansible.galaxy.token.yaml_load", return_value={}):
        config = token.config
    
    assert config["token"] == token_value

def test_galaxy_token_config_with_no_token_sentinel(mock_config_file, monkeypatch):
    monkeypatch.setattr("ansible.galaxy.token.C.GALAXY_TOKEN_PATH", str(mock_config_file))
    token = GalaxyToken(token=NoTokenSentinel)
    
    with patch("ansible.galaxy.token.open", mock_open(read_data="{}")), \
         patch("ansible.galaxy.token.os.path.isfile", return_value=True), \
         patch("ansible.galaxy.token.yaml_load", return_value={}):
        config = token.config
    
    assert config["token"] is None
