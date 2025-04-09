# file lib/ansible/playbook/attribute.py:30-95
# lines [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 95]
# branches ['94->exit', '94->95']

import pytest
from ansible.playbook.attribute import Attribute

def test_attribute_initialization():
    # Test initialization with all parameters
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

def test_attribute_default_mutable_error():
    # Test that a TypeError is raised when default is a mutable type and not callable
    with pytest.raises(TypeError, match='defaults for FieldAttribute may not be mutable, please provide a callable instead'):
        Attribute(
            isa="list",
            default=[],
        )

def test_attribute_default_callable():
    # Test that no error is raised when default is a callable
    attr = Attribute(
        isa="list",
        default=lambda: [],
    )
    assert callable(attr.default)

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup fixture to ensure no side effects
    yield
    mocker.stopall()
