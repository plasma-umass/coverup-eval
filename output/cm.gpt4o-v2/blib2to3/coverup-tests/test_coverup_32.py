# file: src/blib2to3/pytree.py:170-175
# asked: {"lines": [170, 171, 172, 173, 174, 175], "branches": [[171, 172], [171, 173], [173, 174], [173, 175]]}
# gained: {"lines": [170, 171, 172, 173, 174, 175], "branches": [[171, 172], [171, 173], [173, 174], [173, 175]]}

import pytest
from unittest.mock import Mock
from blib2to3.pytree import Node

class TestBase:
    def test_changed_no_parent(self):
        base = Node(type=256, children=[])
        base.was_changed = False
        base.parent = None

        base.changed()

        assert base.was_changed is True

    def test_changed_with_parent(self):
        parent = Mock(spec=Node)
        parent.was_changed = False
        parent.parent = None

        base = Node(type=256, children=[])
        base.was_changed = False
        base.parent = parent

        base.changed()

        parent.changed.assert_called_once()
        assert base.was_changed is True

    def test_changed_already_changed(self):
        base = Node(type=256, children=[])
        base.was_changed = True
        base.parent = None

        base.changed()

        assert base.was_changed is True
