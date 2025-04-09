# file src/blib2to3/pytree.py:421-430
# lines [421, 423, 425, 426, 427, 428, 429]
# branches []

import pytest
from blib2to3.pytree import Base

class MockToken:
    tok_name = {1: 'NAME'}

@pytest.fixture
def mock_token(mocker):
    mocker.patch('blib2to3.pgen2.token', new=MockToken)

def test_leaf_repr(mock_token):
    class Leaf(Base):
        def __init__(self, type, value):
            self.type = type
            self.value = value

        def __repr__(self) -> str:
            """Return a canonical string representation."""
            from blib2to3.pgen2.token import tok_name

            assert self.type is not None
            return "%s(%s, %r)" % (
                self.__class__.__name__,
                tok_name.get(self.type, self.type),
                self.value,
            )

    leaf = Leaf(1, 'test_value')
    repr_str = repr(leaf)
    assert repr_str == "Leaf(NAME, 'test_value')"
