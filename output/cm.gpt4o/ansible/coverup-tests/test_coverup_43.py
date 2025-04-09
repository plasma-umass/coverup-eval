# file lib/ansible/plugins/action/assemble.py:40-81
# lines [40, 43, 44, 45, 46, 48, 49, 50, 51, 52, 53, 55, 56, 59, 60, 63, 64, 66, 67, 70, 71, 73, 74, 75, 76, 78, 80, 81]
# branches ['48->49', '48->80', '49->50', '49->51', '52->53', '52->55', '59->60', '59->63', '63->64', '63->73', '64->66', '64->73', '70->71', '70->73', '75->76', '75->78']

import os
import tempfile
import pytest
import codecs
import re
from unittest import mock
from ansible.plugins.action.assemble import ActionModule
from ansible.module_utils._text import to_text
from ansible import constants as C

@pytest.fixture
def mock_loader():
    loader = mock.Mock()
    loader.get_real_file = mock.Mock(side_effect=lambda x, decrypt: x)
    return loader

@pytest.fixture
def setup_fragments(tmp_path):
    src_path = tmp_path / "fragments"
    src_path.mkdir()
    (src_path / "frag1.txt").write_bytes(b"content1\n")
    (src_path / "frag2.txt").write_bytes(b"content2")
    (src_path / ".hidden").write_bytes(b"hidden")
    return src_path

def test_assemble_from_fragments_with_delimiter(mock_loader, setup_fragments):
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=mock_loader, templar=None, shared_loader_obj=None)
    src_path = str(setup_fragments)
    delimiter = "\\n--DELIM--\\n"
    compiled_regexp = None
    ignore_hidden = True
    decrypt = True

    result_path = action_module._assemble_from_fragments(src_path, delimiter, compiled_regexp, ignore_hidden, decrypt)

    with open(result_path, 'rb') as result_file:
        result_content = result_file.read()

    # The delimiter is escaped, so we need to decode it
    delimiter_decoded = codecs.escape_decode(delimiter)[0]
    expected_content = b"content1\n" + delimiter_decoded + b"\ncontent2"
    assert result_content == expected_content

    os.remove(result_path)

def test_assemble_from_fragments_with_regexp(mock_loader, setup_fragments):
    action_module = ActionModule(task=None, connection=None, play_context=None, loader=mock_loader, templar=None, shared_loader_obj=None)
    src_path = str(setup_fragments)
    delimiter = None
    compiled_regexp = re.compile(r'frag\d+\.txt')
    ignore_hidden = False
    decrypt = True

    result_path = action_module._assemble_from_fragments(src_path, delimiter, compiled_regexp, ignore_hidden, decrypt)

    with open(result_path, 'rb') as result_file:
        result_content = result_file.read()

    expected_content = b"content1\ncontent2"
    assert result_content == expected_content

    os.remove(result_path)
