# file: cookiecutter/replay.py:12-16
# asked: {"lines": [12, 14, 15, 16], "branches": []}
# gained: {"lines": [12, 14, 15, 16], "branches": []}

import os
import pytest

from cookiecutter.replay import get_file_name

@pytest.mark.parametrize("replay_dir, template_name, expected", [
    ("/path/to/replay", "template", "/path/to/replay/template.json"),
    ("/path/to/replay", "template.json", "/path/to/replay/template.json"),
    ("/another/path", "another_template", "/another/path/another_template.json"),
    ("/another/path", "another_template.json", "/another/path/another_template.json"),
])
def test_get_file_name(replay_dir, template_name, expected):
    result = get_file_name(replay_dir, template_name)
    assert result == expected
