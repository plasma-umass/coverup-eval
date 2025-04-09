# file lib/ansible/modules/replace.py:226-313
# lines [227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 238, 239, 242, 243, 244, 245, 247, 248, 249, 250, 252, 253, 255, 256, 258, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278, 280, 281, 282, 284, 286, 287, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 302, 303, 305, 306, 307, 309, 310, 312, 313]
# branches ['252->253', '252->255', '255->256', '255->258', '266->267', '266->268', '268->269', '268->270', '270->271', '270->273', '273->274', '273->284', '276->277', '276->280', '289->290', '289->302', '290->291', '290->292', '294->295', '294->305', '305->306', '305->312', '306->307', '306->309']

import os
import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.replace import main as replace_main
from unittest.mock import patch, mock_open

@pytest.fixture
def mock_ansible_module(mocker):
    module = mocker.patch('ansible.modules.replace.AnsibleModule', autospec=True)
    instance = module.return_value
    instance.params = {}
    instance._diff = False
    instance.check_mode = False
    return instance

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "testfile.txt"
    file.write_text("This is a test file.\nLine to be replaced.\nEnd of file.")
    return file

def test_replace_module_full_coverage(mock_ansible_module, temp_file, mocker):
    params = {
        'path': str(temp_file),
        'regexp': 'Line to be replaced',
        'replace': 'Line has been replaced',
        'after': 'This is a test file.',
        'before': 'End of file.',
        'backup': True,
        'validate': None,
        'encoding': 'utf-8'
    }

    mock_ansible_module.params = params
    mock_ansible_module._diff = True
    mock_ansible_module.check_mode = False

    mocker.patch('ansible.modules.replace.os.path.isdir', return_value=False)
    mocker.patch('ansible.modules.replace.os.path.exists', return_value=True)
    mocker.patch('ansible.modules.replace.os.path.realpath', side_effect=lambda x: x)
    mocker.patch('ansible.modules.replace.open', mock_open(read_data=temp_file.read_text()))
    mocker.patch('ansible.modules.replace.write_changes', autospec=True)
    mocker.patch('ansible.modules.replace.check_file_attrs', return_value=('File attributes checked', True))
    mocker.patch('ansible.modules.replace.to_text', side_effect=lambda x, **kwargs: x)
    mocker.patch('ansible.modules.replace.to_bytes', side_effect=lambda x, **kwargs: x)

    replace_main()

    mock_ansible_module.exit_json.assert_called_once_with(
        msg='File attributes checked',
        changed=True,
        diff={
            'before_header': str(temp_file),
            'before': "This is a test file.\nLine to be replaced.\nEnd of file.",
            'after_header': str(temp_file),
            'after': "This is a test file.\nLine has been replaced.\nEnd of file."
        },
        backup_file=mock_ansible_module.backup_local(str(temp_file))
    )
