# file: lib/ansible/modules/replace.py:213-223
# asked: {"lines": [213, 215, 216, 218, 219, 220, 221, 223], "branches": [[216, 218], [216, 223], [218, 219], [218, 220]]}
# gained: {"lines": [213, 215, 216, 218, 219, 220, 221, 223], "branches": [[216, 218], [216, 223], [218, 219], [218, 220]]}

import pytest
from unittest.mock import Mock
from ansible.modules.replace import check_file_attrs

def test_check_file_attrs_no_change():
    module = Mock()
    module.load_file_common_arguments.return_value = {}
    module.set_file_attributes_if_different.return_value = False

    message, changed = check_file_attrs(module, False, "Initial message")

    assert message == "Initial message"
    assert not changed

def test_check_file_attrs_with_change():
    module = Mock()
    module.load_file_common_arguments.return_value = {}
    module.set_file_attributes_if_different.return_value = True

    message, changed = check_file_attrs(module, False, "Initial message")

    assert message == "Initial messageownership, perms or SE linux context changed"
    assert changed

def test_check_file_attrs_already_changed():
    module = Mock()
    module.load_file_common_arguments.return_value = {}
    module.set_file_attributes_if_different.return_value = True

    message, changed = check_file_attrs(module, True, "Initial message")

    assert message == "Initial message and ownership, perms or SE linux context changed"
    assert changed
