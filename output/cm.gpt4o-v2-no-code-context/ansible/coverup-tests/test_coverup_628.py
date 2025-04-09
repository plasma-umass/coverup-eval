# file: lib/ansible/playbook/base.py:225-227
# asked: {"lines": [225, 226, 227], "branches": []}
# gained: {"lines": [225, 226, 227], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    
    def test_finalized_property(self):
        # Create a subclass to instantiate FieldAttributeBase
        class TestClass(FieldAttributeBase):
            def __init__(self, finalized):
                self._finalized = finalized

        # Instantiate the subclass with a specific value for _finalized
        instance = TestClass(finalized=True)
        
        # Assert that the finalized property returns the correct value
        assert instance.finalized is True

        # Change the value of _finalized and assert again
        instance._finalized = False
        assert instance.finalized is False
