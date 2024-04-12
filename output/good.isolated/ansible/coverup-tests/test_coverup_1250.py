# file lib/ansible/modules/replace.py:213-223
# lines [215, 216, 218, 219, 220, 221, 223]
# branches ['216->218', '216->223', '218->219', '218->220']

import pytest
from ansible.modules.replace import check_file_attrs

def test_check_file_attrs(mocker):
    module_mock = mocker.MagicMock()
    module_mock.params = {'path': '/fake/path'}
    module_mock.load_file_common_arguments.return_value = {}
    module_mock.set_file_attributes_if_different.return_value = True

    message, changed = check_file_attrs(module_mock, True, "content changed")

    assert changed is True
    assert message == "content changed and ownership, perms or SE linux context changed"

    module_mock.set_file_attributes_if_different.assert_called_once_with({}, False)
