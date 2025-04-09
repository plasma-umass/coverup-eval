# file lib/ansible/galaxy/token.py:149-151
# lines [150, 151]
# branches []

import os
import pytest
from ansible.galaxy.token import GalaxyToken
from unittest.mock import MagicMock

# Assuming the GalaxyToken class has an attribute `b_file` and a method `save` that uses an internal `config`.

def test_galaxy_token_save(tmpdir, mocker):
    # Setup
    fake_file = tmpdir.join("token.yml")
    fake_config = {'token': 'fake-token'}

    # Create a GalaxyToken instance with a temporary file path
    token = GalaxyToken()
    token.b_file = str(fake_file)

    # Mock the internal config attribute if it's not directly accessible
    if not hasattr(token, 'config'):
        token.config = fake_config
    else:
        mocker.patch.object(GalaxyToken, 'config', new=fake_config)

    # Mock yaml_dump to actually write to the file since we're checking the file content
    mocker.patch('ansible.galaxy.token.yaml_dump', side_effect=lambda data, stream, **kw: stream.write('token: fake-token'))

    # Exercise
    token.save()

    # Verify
    # Check that the file was created
    assert os.path.exists(str(fake_file))

    # Check the file content
    with open(str(fake_file), 'r') as f:
        content = f.read()
    assert 'fake-token' in content

    # Cleanup
    os.remove(str(fake_file))
