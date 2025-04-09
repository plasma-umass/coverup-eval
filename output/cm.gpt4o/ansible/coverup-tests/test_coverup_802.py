# file lib/ansible/playbook/base.py:122-128
# lines [122, 124]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Base class is defined somewhere in ansible.playbook.base
from ansible.playbook.base import BaseMeta

def test_base_meta():
    # Create a dummy class using BaseMeta
    class DummyClass(metaclass=BaseMeta):
        pass

    # Assert that the metaclass is correctly set
    assert isinstance(DummyClass, BaseMeta)

    # Clean up if necessary (though in this case, there's nothing to clean up)
