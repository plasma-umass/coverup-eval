# file lib/ansible/playbook/role_include.py:68-70
# lines [70]
# branches []

import pytest
from ansible.playbook.role_include import IncludeRole

# Assuming the IncludeRole class has other attributes and methods that are not shown here,
# and that the IncludeRole class is part of a larger Ansible codebase.

# The test function to cover the missing line 70
def test_include_role_get_name(mocker):
    # Create an instance of IncludeRole with the necessary attributes
    include_role_instance = IncludeRole()
    include_role_instance.name = None
    include_role_instance.action = 'include'
    include_role_instance._role_name = 'test_role'

    # Call the method we want to test
    result = include_role_instance.get_name()

    # Assert that the result is as expected, which will execute line 70
    assert result == "include : test_role"
