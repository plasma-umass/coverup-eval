# file lib/ansible/modules/lineinfile.py:284-294
# lines [286, 287, 289, 290, 291, 292, 294]
# branches ['287->289', '287->294', '289->290', '289->291']

import pytest
from ansible.modules.lineinfile import check_file_attrs

def test_check_file_attrs(mocker):
    module_mock = mocker.MagicMock()
    module_mock.params = {'path': '/fake/path'}
    module_mock.load_file_common_arguments.return_value = {}
    module_mock.set_fs_attributes_if_different.return_value = True

    message, changed = check_file_attrs(module_mock, True, "content changed", None)

    assert changed is True
    assert message == "content changed and ownership, perms or SE linux context changed"

    module_mock.set_fs_attributes_if_different.assert_called_once_with({}, False, diff=None)

    # Cleanup is not necessary as we are using mocks and not creating any real files
