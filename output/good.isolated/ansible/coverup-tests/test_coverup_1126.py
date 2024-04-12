# file lib/ansible/playbook/block.py:295-359
# lines [300, 301, 302, 303, 306, 307, 309, 311, 312, 313, 314, 315, 317, 318, 319, 321, 322, 323, 324, 325, 326, 327, 328, 330, 332, 333, 334, 335, 336, 337, 338, 340, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 353, 354, 355, 356, 357, 359]
# branches ['306->307', '306->309', '311->312', '311->324', '313->314', '313->324', '314->315', '314->317', '318->319', '318->321', '324->325', '324->346', '327->328', '327->330', '333->334', '333->346', '335->336', '335->346', '337->338', '337->340', '342->335', '342->343', '346->347', '346->359', '349->350', '349->359', '350->351', '350->353']

import pytest
from ansible.playbook.block import Block
from ansible.playbook.attribute import Attribute
from ansible.playbook.base import Base
from ansible.utils.sentinel import Sentinel

# Mock classes to simulate the behavior of parent, role, and play
class MockParent(Base):
    def __init__(self, statically_loaded=True, attributes=None):
        self.statically_loaded = statically_loaded
        self._attributes = attributes or {}

class MockRole(Base):
    def __init__(self, attributes=None):
        self._attributes = attributes or {}

class MockPlay(Base):
    def __init__(self, attributes=None):
        self._attributes = attributes or {}

@pytest.fixture
def block():
    # Create a Block instance with mock _valid_attrs
    b = Block()
    b._valid_attrs = {
        'test_attr': Attribute(isa='list', default=list, extend=True, prepend=False)
    }
    return b

@pytest.fixture
def parent():
    # Create a MockParent instance with some attributes
    return MockParent(attributes={'test_attr': ['parent_value']})

@pytest.fixture
def role():
    # Create a MockRole instance with some attributes
    return MockRole(attributes={'test_attr': ['role_value']})

@pytest.fixture
def play():
    # Create a MockPlay instance with some attributes
    return MockPlay(attributes={'test_attr': ['play_value']})

def test_get_parent_attribute_extend_prepend(block, parent, role, play, mocker):
    # Set up the block with parent, role, and play
    block._parent = parent
    block._role = role
    block._play = play

    # Set the block's attribute to Sentinel to trigger the retrieval from parent, role, and play
    block._attributes['test_attr'] = Sentinel

    # Test the retrieval and extension of the attribute from parent, role, and play
    value = block._get_parent_attribute('test_attr')
    assert value == ['parent_value', 'role_value', 'play_value'], "The attribute should be extended from parent, role, and play"

    # Clean up after the test
    mocker.stopall()
