# file lib/ansible/modules/lineinfile.py:284-294
# lines [284, 286, 287, 289, 290, 291, 292, 294]
# branches ['287->289', '287->294', '289->290', '289->291']

import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule

def test_check_file_attrs(mocker):
    # Mock the AnsibleModule and its methods
    module = mocker.Mock(spec=AnsibleModule)
    module.params = {}
    module.load_file_common_arguments.return_value = {}
    module.set_fs_attributes_if_different.return_value = True

    # Import the function to be tested
    from ansible.modules.lineinfile import check_file_attrs

    # Test case where attributes are different
    message, changed = check_file_attrs(module, False, "Initial message", {})
    assert changed is True
    assert message == "Initial messageownership, perms or SE linux context changed"

    # Test case where attributes are different and changed is already True
    message, changed = check_file_attrs(module, True, "Initial message", {})
    assert changed is True
    assert message == "Initial message and ownership, perms or SE linux context changed"

    # Test case where attributes are not different
    module.set_fs_attributes_if_different.return_value = False
    message, changed = check_file_attrs(module, False, "Initial message", {})
    assert changed is False
    assert message == "Initial message"
