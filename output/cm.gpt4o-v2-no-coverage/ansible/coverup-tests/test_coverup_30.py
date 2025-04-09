# file: lib/ansible/plugins/action/assemble.py:40-81
# asked: {"lines": [40, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55, 56, 59, 60, 63, 64, 66, 67, 70, 71, 73, 74, 75, 76, 78, 80, 81], "branches": [[48, 49], [48, 80], [49, 50], [49, 51], [52, 53], [52, 55], [59, 60], [59, 63], [63, 64], [63, 73], [64, 66], [64, 73], [70, 71], [70, 73], [75, 76], [75, 78]]}
# gained: {"lines": [40, 43, 44, 45, 46, 48, 49, 51, 52, 53, 55, 56, 59, 63, 64, 66, 67, 70, 71, 73, 74, 75, 76, 78, 80, 81], "branches": [[48, 49], [48, 80], [49, 51], [52, 53], [52, 55], [59, 63], [63, 64], [63, 73], [64, 66], [70, 71], [75, 76], [75, 78]]}

import os
import tempfile
import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.plugins.action.assemble import ActionModule
from ansible import constants as C

@pytest.fixture
def action_module():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return ActionModule(task, connection, play_context, loader, templar, shared_loader_obj)

def test_assemble_from_fragments(action_module, monkeypatch):
    src_path = tempfile.mkdtemp()
    fragment_files = ['fragment1.txt', 'fragment2.txt', '.hidden_fragment']
    fragment_content = {
        'fragment1.txt': b'content1\n',
        'fragment2.txt': b'content2',
        '.hidden_fragment': b'hidden'
    }

    for filename, content in fragment_content.items():
        with open(os.path.join(src_path, filename), 'wb') as f:
            f.write(content)

    def mock_get_real_file(path, decrypt=True):
        return path

    monkeypatch.setattr(action_module._loader, 'get_real_file', mock_get_real_file)

    temp_dir = tempfile.mkdtemp()
    monkeypatch.setattr(C, 'DEFAULT_LOCAL_TMP', temp_dir)

    result_path = action_module._assemble_from_fragments(src_path, delimiter='--', ignore_hidden=True)

    with open(result_path, 'rb') as result_file:
        result_content = result_file.read()

    expected_content = b'content1\n--\ncontent2'
    assert result_content == expected_content

    os.remove(result_path)
    for filename in fragment_files:
        os.remove(os.path.join(src_path, filename))
    os.rmdir(src_path)
    os.rmdir(temp_dir)
