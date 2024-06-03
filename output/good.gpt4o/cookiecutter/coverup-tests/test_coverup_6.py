# file cookiecutter/replay.py:12-16
# lines [12, 14, 15, 16]
# branches []

import os
import pytest
from cookiecutter.replay import get_file_name

def test_get_file_name(mocker):
    # Mock the os.path.join to ensure it behaves as expected
    mocker.patch('os.path.join', side_effect=lambda *args: '/'.join(args))

    replay_dir = 'replay_directory'
    template_name_with_json = 'template.json'
    template_name_without_json = 'template'

    # Test when template_name ends with '.json'
    result_with_json = get_file_name(replay_dir, template_name_with_json)
    assert result_with_json == 'replay_directory/template.json'

    # Test when template_name does not end with '.json'
    result_without_json = get_file_name(replay_dir, template_name_without_json)
    assert result_without_json == 'replay_directory/template.json'
