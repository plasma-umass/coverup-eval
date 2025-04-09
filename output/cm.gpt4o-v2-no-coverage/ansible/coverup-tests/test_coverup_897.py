# file: lib/ansible/playbook/attribute.py:118-119
# asked: {"lines": [118, 119], "branches": []}
# gained: {"lines": [118, 119], "branches": []}

import pytest
from ansible.playbook.attribute import FieldAttribute, Attribute

def test_field_attribute_initialization():
    # Test initialization with default values
    field_attr = FieldAttribute()
    assert field_attr.isa is None
    assert field_attr.private is False
    assert field_attr.default is None
    assert field_attr.required is False
    assert field_attr.listof is None
    assert field_attr.priority == 0
    assert field_attr.class_type is None
    assert field_attr.always_post_validate is False
    assert field_attr.inherit is True
    assert field_attr.alias is None
    assert field_attr.extend is False
    assert field_attr.prepend is False
    assert field_attr.static is False

    # Test initialization with custom values
    field_attr = FieldAttribute(isa="str", private=True, default="default", required=True, listof="int", priority=1, class_type=dict, always_post_validate=True, inherit=False, alias="alias", extend=True, prepend=True, static=True)
    assert field_attr.isa == "str"
    assert field_attr.private is True
    assert field_attr.default == "default"
    assert field_attr.required is True
    assert field_attr.listof == "int"
    assert field_attr.priority == 1
    assert field_attr.class_type == dict
    assert field_attr.always_post_validate is True
    assert field_attr.inherit is False
    assert field_attr.alias == "alias"
    assert field_attr.extend is True
    assert field_attr.prepend is True
    assert field_attr.static is True

    # Test TypeError for mutable default with isa in _CONTAINERS
    with pytest.raises(TypeError):
        FieldAttribute(isa="list", default=[])

    with pytest.raises(TypeError):
        FieldAttribute(isa="dict", default={})

    with pytest.raises(TypeError):
        FieldAttribute(isa="set", default=set())

    # Test callable default
    field_attr = FieldAttribute(default=lambda: [])
    assert callable(field_attr.default)

    field_attr = FieldAttribute(default=lambda: {})
    assert callable(field_attr.default)

    field_attr = FieldAttribute(default=lambda: set())
    assert callable(field_attr.default)
