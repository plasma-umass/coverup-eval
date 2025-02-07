# file: lib/ansible/parsing/dataloader.py:197-229
# asked: {"lines": [200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}
# gained: {"lines": [200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}

import os
import re
import pytest
from unittest.mock import patch
from ansible.module_utils._text import to_bytes
from ansible.utils.path import unfrackpath
from ansible.parsing.dataloader import DataLoader

# Mock the RE_TASKS regex pattern
RE_TASKS = re.compile(u'(?:^|%s)+tasks%s?$' % (os.path.sep, os.path.sep))

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_role_with_tasks_in_path(dataloader):
    path = 'some/tasks/path'
    b_path = to_bytes(path, errors='surrogate_or_strict')
    b_path_dirname = os.path.dirname(b_path)
    b_upath = to_bytes(unfrackpath(path, follow=False), errors='surrogate_or_strict')

    untasked_paths = (
        os.path.join(b_path, b'main.yml'),
        os.path.join(b_path, b'main.yaml'),
        os.path.join(b_path, b'main'),
    )
    tasked_paths = (
        os.path.join(b_upath, b'tasks/main.yml'),
        os.path.join(b_upath, b'tasks/main.yaml'),
        os.path.join(b_upath, b'tasks/main'),
        os.path.join(b_upath, b'meta/main.yml'),
        os.path.join(b_upath, b'meta/main.yaml'),
        os.path.join(b_upath, b'meta/main'),
        os.path.join(b_path_dirname, b'tasks/main.yml'),
        os.path.join(b_path_dirname, b'tasks/main.yaml'),
        os.path.join(b_path_dirname, b'tasks/main'),
        os.path.join(b_path_dirname, b'meta/main.yml'),
        os.path.join(b_path_dirname, b'meta/main.yaml'),
        os.path.join(b_path_dirname, b'meta/main'),
    )

    with patch('os.path.exists', return_value=True):
        assert dataloader._is_role(path) is True

def test_is_role_without_tasks_in_path(dataloader):
    path = 'some/other/path'
    b_path = to_bytes(path, errors='surrogate_or_strict')
    b_path_dirname = os.path.dirname(b_path)
    b_upath = to_bytes(unfrackpath(path, follow=False), errors='surrogate_or_strict')

    untasked_paths = (
        os.path.join(b_path, b'main.yml'),
        os.path.join(b_path, b'main.yaml'),
        os.path.join(b_path, b'main'),
    )
    tasked_paths = (
        os.path.join(b_upath, b'tasks/main.yml'),
        os.path.join(b_upath, b'tasks/main.yaml'),
        os.path.join(b_upath, b'tasks/main'),
        os.path.join(b_upath, b'meta/main.yml'),
        os.path.join(b_upath, b'meta/main.yaml'),
        os.path.join(b_upath, b'meta/main'),
        os.path.join(b_path_dirname, b'tasks/main.yml'),
        os.path.join(b_path_dirname, b'tasks/main.yaml'),
        os.path.join(b_path_dirname, b'tasks/main'),
        os.path.join(b_path_dirname, b'meta/main.yml'),
        os.path.join(b_path_dirname, b'meta/main.yaml'),
        os.path.join(b_path_dirname, b'meta/main'),
    )

    with patch('os.path.exists', return_value=False):
        assert dataloader._is_role(path) is False
