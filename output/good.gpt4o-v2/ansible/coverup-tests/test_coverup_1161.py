# file: lib/ansible/galaxy/token.py:123-140
# asked: {"lines": [124, 125, 127, 128, 129, 131, 132, 134, 136, 137, 138, 140], "branches": [[125, 127], [125, 131], [136, 137], [136, 140]]}
# gained: {"lines": [124, 125, 127, 128, 129, 131, 132, 134, 136, 137, 138, 140], "branches": [[125, 127], [125, 131], [136, 137], [136, 140]]}

import os
import pytest
from unittest import mock
from ansible.module_utils.common.yaml import yaml_load
from ansible.module_utils._text import to_bytes, to_text
from ansible import constants as C
from ansible.utils.display import Display
from ansible.galaxy.token import GalaxyToken

@pytest.fixture
def mock_display_vvv():
    with mock.patch('ansible.utils.display.Display.vvv') as mock_vvv:
        yield mock_vvv

@pytest.fixture
def galaxy_token(tmp_path):
    token_path = tmp_path / "galaxy_token.yml"
    with mock.patch.object(C, 'GALAXY_TOKEN_PATH', str(token_path)):
        yield GalaxyToken()

def test_read_creates_file_if_not_exists(galaxy_token, mock_display_vvv):
    assert not os.path.isfile(galaxy_token.b_file)
    config = galaxy_token._read()
    assert os.path.isfile(galaxy_token.b_file)
    assert config == {}
    mock_display_vvv.assert_called_with('Created %s' % to_text(galaxy_token.b_file))

def test_read_opens_existing_file(galaxy_token, mock_display_vvv):
    with open(galaxy_token.b_file, 'w') as f:
        f.write('token: test_token')
    config = galaxy_token._read()
    assert config == {'token': 'test_token'}
    mock_display_vvv.assert_called_with('Opened %s' % to_text(galaxy_token.b_file))

def test_read_malformed_file(galaxy_token, mock_display_vvv):
    with open(galaxy_token.b_file, 'w') as f:
        f.write('malformed content')
    config = galaxy_token._read()
    assert config == {}
    mock_display_vvv.assert_called_with('Galaxy token file %s malformed, unable to read it' % to_text(galaxy_token.b_file))
