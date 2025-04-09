# file lib/ansible/plugins/action/copy.py:231-386
# lines [231, 233, 234, 235, 237, 238, 241, 242, 243, 244, 245, 246, 250, 251, 252, 257, 258, 260, 263, 265, 267, 269, 270, 271, 272, 275, 276, 278, 280, 283, 285, 288, 289, 291, 292, 293, 294, 297, 299, 301, 302, 304, 307, 308, 315, 316, 318, 320, 326, 327, 328, 329, 330, 331, 332, 335, 336, 338, 339, 341, 346, 347, 349, 350, 355, 356, 357, 358, 361, 362, 363, 364, 365, 366, 367, 371, 372, 373, 374, 376, 377, 380, 382, 383, 385, 386]
# branches ['251->252', '251->257', '257->258', '257->260', '265->267', '265->278', '267->269', '267->275', '278->280', '278->283', '285->288', '285->346', '288->289', '288->291', '291->292', '291->297', '301->302', '301->304', '315->316', '315->318', '318->320', '318->326', '335->336', '335->338', '338->339', '338->341', '349->350', '349->355', '355->356', '355->361', '357->358', '357->361', '376->377', '376->380', '382->383', '382->385']

import os
import pytest
import stat
from ansible.errors import AnsibleFileNotFound
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
from ansible.plugins.action.copy import ActionModule
from ansible.utils.hashing import checksum
from ansible.module_utils.parsing.convert_bool import boolean
from unittest.mock import MagicMock, patch

# Define a fixture for the ActionModule instance
@pytest.fixture
def action_module():
    mock_loader = MagicMock()
    mock_loader.get_real_file = MagicMock()
    mock_connection = MagicMock()
    mock_connection._shell.join_path = os.path.join
    mock_connection._shell.tmpdir = '/tmp'
    mock_connection._shell.path_has_trailing_slash = lambda x: x.endswith('/')
    mock_task = MagicMock()
    mock_task.args = {}
    return ActionModule(task=mock_task, connection=mock_connection, play_context=None, loader=mock_loader, templar=None, shared_loader_obj=None)

# Define a fixture for cleanup
@pytest.fixture
def cleanup_files():
    created_files = []

    yield created_files

    for file in created_files:
        if os.path.exists(file):
            os.remove(file)

# Test function to cover missing lines/branches
def test_copy_file_not_exists(action_module, cleanup_files, mocker):
    source_full = '/fake/source/path'
    source_rel = 'source_rel'
    dest = '/fake/dest/path'
    task_vars = {}
    follow = False

    # Mock methods to simulate file not existing
    action_module._loader.get_real_file.side_effect = AnsibleFileNotFound('File not found')
    action_module._execute_remote_stat = MagicMock(return_value={'exists': False})
    action_module._remove_tempfile_if_content_defined = MagicMock()
    action_module._transfer_file = MagicMock()
    action_module._fixup_perms2 = MagicMock()
    action_module._execute_module = MagicMock()

    # Create a temporary file to act as the source file
    temp_source = '/tmp/temp_source_file'
    cleanup_files.append(temp_source)
    with open(temp_source, 'w') as f:
        f.write('content')

    # Mock checksum function
    mocker.patch('ansible.plugins.action.copy.checksum', return_value='fake-checksum')

    # Run the method
    result = action_module._copy_file(temp_source, source_rel, None, None, dest, task_vars, follow)

    # Assertions
    assert result['failed']
    assert 'could not find src=' in result['msg']
    assert action_module._loader.get_real_file.called
    assert not action_module._execute_remote_stat.called
    assert not action_module._remove_tempfile_if_content_defined.called
    assert not action_module._transfer_file.called
    assert not action_module._fixup_perms2.called
    assert not action_module._execute_module.called
