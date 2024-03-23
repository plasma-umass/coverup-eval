# file lib/ansible/inventory/group.py:205-222
# lines [205, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222]
# branches ['212->exit', '212->213', '217->218', '217->221', '218->217', '218->219', '221->212', '221->222']

import pytest
from ansible.errors import AnsibleError
from ansible.inventory.group import Group
from ansible.module_utils._text import to_native

class MockGroup(Group):
    def __init__(self, name):
        super(MockGroup, self).__init__(name)
        self.child_groups = set()

def test_group_recursive_dependency_loop(mocker):
    # Setup
    group_a = MockGroup('a')
    group_b = MockGroup('b')
    group_c = MockGroup('c')

    # Create a recursive loop
    group_a.child_groups.add(group_b)
    group_b.child_groups.add(group_c)
    group_c.child_groups.add(group_a)  # This creates the loop

    # Assertion
    with pytest.raises(AnsibleError) as excinfo:
        group_a._check_children_depth()
    assert "has a recursive dependency loop" in str(excinfo.value)

    # Cleanup is not necessary as we are using mock objects that are not persisted
