# file src/blib2to3/pytree.py:369-379
# lines [369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379]
# branches ['375->376', '375->379']

import pytest
from blib2to3.pytree import Node, Leaf

@pytest.fixture
def mock_node():
    node = Node(type=256, children=[Leaf(type=1, value='a'), Leaf(type=2, value='b')])
    return node

def test_update_sibling_maps(mock_node):
    mock_node.update_sibling_maps()
    
    # Assertions to check if the sibling maps are correctly updated
    children_ids = [id(child) for child in mock_node.children]
    assert mock_node.prev_sibling_map[children_ids[0]] is None
    assert mock_node.prev_sibling_map[children_ids[1]] == mock_node.children[0]
    assert mock_node.next_sibling_map[children_ids[0]] == mock_node.children[1]
    assert mock_node.next_sibling_map.get(children_ids[1]) is None
