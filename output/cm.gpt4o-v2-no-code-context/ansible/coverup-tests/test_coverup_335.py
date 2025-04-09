# file: lib/ansible/modules/lineinfile.py:284-294
# asked: {"lines": [284, 286, 287, 289, 290, 291, 292, 294], "branches": [[287, 289], [287, 294], [289, 290], [289, 291]]}
# gained: {"lines": [284, 286, 287, 289, 290, 291, 292, 294], "branches": [[287, 289], [287, 294], [289, 290], [289, 291]]}

import pytest
from unittest.mock import Mock

# Assuming the function check_file_attrs is part of a class or module named LineInFile
# and module is an instance of AnsibleModule or similar.

def test_check_file_attrs_no_change(monkeypatch):
    module = Mock()
    module.load_file_common_arguments.return_value = {}
    module.set_fs_attributes_if_different.return_value = False

    from ansible.modules.lineinfile import check_file_attrs

    message, changed = check_file_attrs(module, False, "Initial message", {})

    assert message == "Initial message"
    assert changed is False

def test_check_file_attrs_with_change(monkeypatch):
    module = Mock()
    module.load_file_common_arguments.return_value = {}
    module.set_fs_attributes_if_different.return_value = True

    from ansible.modules.lineinfile import check_file_attrs

    message, changed = check_file_attrs(module, False, "Initial message", {})

    assert message == "Initial messageownership, perms or SE linux context changed"
    assert changed is True

def test_check_file_attrs_already_changed(monkeypatch):
    module = Mock()
    module.load_file_common_arguments.return_value = {}
    module.set_fs_attributes_if_different.return_value = True

    from ansible.modules.lineinfile import check_file_attrs

    message, changed = check_file_attrs(module, True, "Initial message", {})

    assert message == "Initial message and ownership, perms or SE linux context changed"
    assert changed is True
