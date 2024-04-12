# file src/blib2to3/pytree.py:421-430
# lines [421, 423, 425, 426, 427, 428, 429]
# branches []

import pytest
from blib2to3.pytree import Leaf
from blib2to3.pgen2 import token

@pytest.fixture
def leaf_instance():
    leaf = Leaf(token.NAME, 'example')
    yield leaf
    # No cleanup needed for this simple object

def test_leaf_repr(leaf_instance):
    expected_repr = "Leaf(%s, %r)" % (token.tok_name[token.NAME], 'example')
    assert repr(leaf_instance) == expected_repr
