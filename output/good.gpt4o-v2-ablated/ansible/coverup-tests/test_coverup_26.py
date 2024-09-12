# file: lib/ansible/playbook/attribute.py:30-95
# asked: {"lines": [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95], "branches": [[94, 0], [94, 95]]}
# gained: {"lines": [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95], "branches": [[94, 0], [94, 95]]}

import pytest
from ansible.playbook.attribute import Attribute

def test_attribute_initialization():
    attr = Attribute(
        isa="string",
        private=True,
        default="default_value",
        required=True,
        listof="string",
        priority=1,
        class_type=str,
        always_post_validate=True,
        inherit=False,
        alias="alias_name",
        extend=True,
        prepend=True,
        static=True,
    )
    
    assert attr.isa == "string"
    assert attr.private is True
    assert attr.default == "default_value"
    assert attr.required is True
    assert attr.listof == "string"
    assert attr.priority == 1
    assert attr.class_type == str
    assert attr.always_post_validate is True
    assert attr.inherit is False
    assert attr.alias == "alias_name"
    assert attr.extend is True
    assert attr.prepend is True
    assert attr.static is True

def test_attribute_default_none():
    attr = Attribute()
    
    assert attr.isa is None
    assert attr.private is False
    assert attr.default is None
    assert attr.required is False
    assert attr.listof is None
    assert attr.priority == 0
    assert attr.class_type is None
    assert attr.always_post_validate is False
    assert attr.inherit is True
    assert attr.alias is None
    assert attr.extend is False
    assert attr.prepend is False
    assert attr.static is False

def test_attribute_mutable_default_error():
    with pytest.raises(TypeError, match="defaults for FieldAttribute may not be mutable, please provide a callable instead"):
        Attribute(default=[], isa="list")

def test_attribute_callable_default():
    attr = Attribute(default=lambda: [], isa="list")
    assert callable(attr.default)
    assert attr.isa == "list"
