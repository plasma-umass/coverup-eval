# file src/blib2to3/pytree.py:170-175
# lines [170, 171, 172, 173, 174, 175]
# branches ['171->172', '171->173', '173->174', '173->175']

import pytest
from blib2to3.pytree import Base

class Derived(Base):
    def __init__(self):
        self.was_changed = False
        self.parent = None

@pytest.fixture
def base_instance():
    return Derived()

def test_base_changed_without_parent(base_instance):
    assert not base_instance.was_changed
    base_instance.changed()
    assert base_instance.was_changed

def test_base_changed_with_parent(mocker):
    parent_instance = mocker.Mock(spec=Base)
    child_instance = Derived()
    child_instance.parent = parent_instance

    assert not child_instance.was_changed
    assert not parent_instance.changed.called

    child_instance.changed()

    assert child_instance.was_changed
    parent_instance.changed.assert_called_once()
