# file lib/ansible/galaxy/token.py:123-140
# lines [123, 124, 125, 127, 128, 129, 131, 132, 134, 136, 137, 138, 140]
# branches ['125->127', '125->131', '136->137', '136->140']

import os
import pytest
import yaml
from unittest import mock
from ansible.galaxy.token import GalaxyToken
from ansible.utils.display import Display

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.galaxy.token.display')

@pytest.fixture
def galaxy_token(tmp_path):
    class TestGalaxyToken(GalaxyToken):
        def __init__(self, b_file):
            self.b_file = b_file

    return TestGalaxyToken(tmp_path / "token_file.yaml")

def test_read_creates_file_if_not_exists(galaxy_token, mock_display):
    assert not os.path.isfile(galaxy_token.b_file)
    config = galaxy_token._read()
    assert os.path.isfile(galaxy_token.b_file)
    assert config == {}
    mock_display.vvv.assert_any_call('Created %s' % galaxy_token.b_file)

def test_read_opens_existing_file(galaxy_token, mock_display):
    with open(galaxy_token.b_file, 'w') as f:
        yaml.dump({'token': 'test'}, f)
    config = galaxy_token._read()
    assert config == {'token': 'test'}
    mock_display.vvv.assert_any_call('Opened %s' % galaxy_token.b_file)

def test_read_malformed_file(galaxy_token, mock_display):
    with open(galaxy_token.b_file, 'w') as f:
        f.write('not a dict')
    config = galaxy_token._read()
    assert config == {}
    mock_display.vvv.assert_any_call('Galaxy token file %s malformed, unable to read it' % galaxy_token.b_file)
