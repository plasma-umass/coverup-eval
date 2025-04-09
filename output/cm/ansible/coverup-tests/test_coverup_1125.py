# file lib/ansible/modules/replace.py:226-313
# lines [227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 238, 239, 242, 243, 244, 245, 247, 248, 249, 250, 252, 253, 255, 256, 258, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278, 280, 281, 282, 284, 286, 287, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 302, 303, 305, 306, 307, 309, 310, 312, 313]
# branches ['252->253', '252->255', '255->256', '255->258', '266->267', '266->268', '268->269', '268->270', '270->271', '270->273', '273->274', '273->284', '276->277', '276->280', '289->290', '289->302', '290->291', '290->292', '294->295', '294->305', '305->306', '305->312', '306->307', '306->309']

import os
import pytest
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.replace import main as replace_main

@pytest.fixture
def fake_ansible_module(mocker):
    mocked_module = mocker.MagicMock(spec=AnsibleModule)
    mocked_module.params = {
        'path': '/tmp/test_replace',
        'regexp': 'original',
        'replace': 'replaced',
        'after': 'start',
        'before': 'end',
        'backup': False,
        'validate': None,
        'encoding': 'utf-8',
    }
    mocked_module.check_mode = False
    mocked_module._diff = True
    mocker.patch('ansible.modules.replace.AnsibleModule', return_value=mocked_module)
    return mocked_module

@pytest.fixture
def test_file(tmp_path):
    test_file = tmp_path / "test_replace"
    test_file.write_text(u"start\noriginal\ndata\nend", encoding='utf-8')
    return str(test_file)

def test_replace_module(fake_ansible_module, test_file, mocker):
    fake_ansible_module.params['path'] = test_file
    mocker.patch('ansible.modules.replace.os.path.exists', return_value=True)
    mocker.patch('ansible.modules.replace.os.path.isdir', return_value=False)
    mocker.patch('ansible.modules.replace.os.path.realpath', return_value=test_file)
    mocker.patch('ansible.modules.replace.write_changes')
    check_file_attrs_mock = mocker.patch('ansible.modules.replace.check_file_attrs', return_value=('1 replacements made', True))

    replace_main()

    fake_ansible_module.fail_json.assert_not_called()
    fake_ansible_module.exit_json.assert_called_once()
    exit_call_args = fake_ansible_module.exit_json.call_args[1]
    assert exit_call_args['changed'] is True
    assert 'replacements made' in exit_call_args['msg']
    assert 'diff' in exit_call_args
    assert exit_call_args['diff']['before'] == "start\noriginal\ndata\nend"
    assert exit_call_args['diff']['after'] == "start\nreplaced\ndata\nend"
