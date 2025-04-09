# file: lib/ansible/plugins/action/include_vars.py:27-46
# asked: {"lines": [27, 28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45], "branches": [[28, 29], [28, 31], [31, 32], [31, 34], [36, 37], [36, 39], [39, 40], [39, 42], [42, 0], [42, 43]]}
# gained: {"lines": [27, 28, 29, 31, 32, 34, 36, 37, 39, 40, 42, 43, 44, 45], "branches": [[28, 29], [28, 31], [31, 32], [31, 34], [36, 37], [36, 39], [39, 40], [39, 42], [42, 0], [42, 43]]}

import pytest
import re
from ansible.plugins.action.include_vars import ActionModule
from ansible.module_utils.six import string_types

class MockActionModule(ActionModule):
    def __init__(self, depth=None, files_matching=None, ignore_files=None):
        self.depth = depth
        self.files_matching = files_matching
        self.ignore_files = ignore_files

@pytest.mark.parametrize("depth, expected_depth", [
    (None, 0),
    (1, 1),
])
def test_set_dir_defaults_depth(depth, expected_depth):
    action_module = MockActionModule(depth=depth)
    action_module._set_dir_defaults()
    assert action_module.depth == expected_depth

@pytest.mark.parametrize("files_matching, expected_matcher", [
    (None, None),
    ("test", re.compile("test")),
])
def test_set_dir_defaults_files_matching(files_matching, expected_matcher):
    action_module = MockActionModule(files_matching=files_matching)
    action_module._set_dir_defaults()
    assert action_module.matcher == expected_matcher

@pytest.mark.parametrize("ignore_files, expected_ignore_files", [
    (None, []),
    ("file1 file2", ["file1", "file2"]),
    (["file1", "file2"], ["file1", "file2"]),
])
def test_set_dir_defaults_ignore_files(ignore_files, expected_ignore_files):
    action_module = MockActionModule(ignore_files=ignore_files)
    action_module._set_dir_defaults()
    assert action_module.ignore_files == expected_ignore_files

def test_set_dir_defaults_ignore_files_dict():
    action_module = MockActionModule(ignore_files={"key": "value"})
    result = action_module._set_dir_defaults()
    assert result == {'failed': True, 'message': "{'key': 'value'} must be a list"}
