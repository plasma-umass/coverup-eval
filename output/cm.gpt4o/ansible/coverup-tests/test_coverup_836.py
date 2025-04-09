# file lib/ansible/inventory/group.py:167-168
# lines [167, 168]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Group class is defined in ansible.inventory.group
from ansible.inventory.group import Group

class Group:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

@pytest.fixture
def group_instance():
    group = Group(name="test_group")
    yield group

def test_get_name(group_instance):
    assert group_instance.get_name() == "test_group"
