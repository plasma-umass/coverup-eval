# file src/blib2to3/pytree.py:472-475
# lines [472, 473, 474, 475]
# branches []

import pytest
from blib2to3.pytree import Base

class TestLeaf:
    def test_prefix_setter(self, mocker):
        class Leaf(Base):
            def __init__(self):
                self._prefix = ""
                self._changed = False

            def changed(self):
                self._changed = True

            @property
            def prefix(self):
                return self._prefix

            @prefix.setter
            def prefix(self, prefix) -> None:
                self.changed()
                self._prefix = prefix

        leaf = Leaf()
        assert leaf._changed == False
        assert leaf._prefix == ""

        leaf.prefix = "new_prefix"
        assert leaf._changed == True
        assert leaf._prefix == "new_prefix"
