# file lib/ansible/playbook/attribute.py:30-95
# lines [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95]
# branches ['94->exit', '94->95']

import pytest
from ansible.playbook.attribute import Attribute

# Assuming the _CONTAINERS constant is defined somewhere in the module
# If not, you would need to import or define it accordingly
_CONTAINERS = ('list', 'dict', 'set')

def test_attribute_default_mutable_error():
    with pytest.raises(TypeError):
        Attribute(isa='list', default=[])

def test_attribute_default_mutable_no_error():
    # Using a callable for default, which should not raise an error
    attr = Attribute(isa='list', default=lambda: [])
    assert callable(attr.default)
