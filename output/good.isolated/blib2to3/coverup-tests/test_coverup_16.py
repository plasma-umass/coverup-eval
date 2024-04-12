# file src/blib2to3/pytree.py:593-638
# lines [593, 594, 596, 597, 598, 611, 612, 613, 614, 615, 616, 617, 619, 621, 622, 623, 625, 638]
# branches ['611->612', '611->613', '613->614', '613->615', '621->622', '621->623']

import pytest
from blib2to3.pytree import LeafPattern, Leaf, Node

def test_leaf_pattern_match_with_type_and_content(mocker):
    # Mock a Leaf node with specific type and value
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.type = 100
    mock_leaf.value = "mock_content"

    # Create a LeafPattern that should match the mock_leaf
    pattern = LeafPattern(type=100, content="mock_content")

    # Assert that the pattern matches the leaf
    assert pattern.match(mock_leaf)

def test_leaf_pattern_match_with_type_no_content(mocker):
    # Mock a Leaf node with specific type
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.type = 100
    mock_leaf.value = "any_content"

    # Create a LeafPattern with only a type, no content
    pattern = LeafPattern(type=100)

    # Assert that the pattern matches the leaf regardless of content
    assert pattern.match(mock_leaf)

def test_leaf_pattern_match_with_content_no_type(mocker):
    # Mock a Leaf node with any type and specific value
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.type = 255  # Any type less than 256
    mock_leaf.value = "specific_content"

    # Create a LeafPattern with only content, no type
    pattern = LeafPattern(content="specific_content")

    # Assert that the pattern matches the leaf regardless of type
    assert pattern.match(mock_leaf)

def test_leaf_pattern_no_match_due_to_type(mocker):
    # Mock a Leaf node with a different type than the pattern
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.type = 200
    mock_leaf.value = "mock_content"

    # Create a LeafPattern with a specific type that doesn't match the leaf's type
    pattern = LeafPattern(type=100, content="mock_content")

    # Assert that the pattern does not match the leaf
    assert not pattern.match(mock_leaf)

def test_leaf_pattern_no_match_due_to_content(mocker):
    # Mock a Leaf node with a different content than the pattern
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.type = 100
    mock_leaf.value = "different_content"

    # Create a LeafPattern with a specific content that doesn't match the leaf's content
    pattern = LeafPattern(type=100, content="mock_content")

    # Assert that the pattern does not match the leaf
    assert not pattern.match(mock_leaf)

def test_leaf_pattern_no_match_due_to_node_type(mocker):
    # Mock a Node instead of a Leaf
    mock_node = mocker.Mock(spec=Node)
    mock_node.type = 100
    mock_node.value = "mock_content"

    # Create a LeafPattern that should match a Leaf, not a Node
    pattern = LeafPattern(type=100, content="mock_content")

    # Assert that the pattern does not match the node
    assert not pattern.match(mock_node)

def test_leaf_pattern_match_with_name(mocker):
    # Mock a Leaf node with specific type and value
    mock_leaf = mocker.Mock(spec=Leaf)
    mock_leaf.type = 100
    mock_leaf.value = "mock_content"

    # Create a LeafPattern with a name
    pattern = LeafPattern(type=100, content="mock_content", name="mock_name")

    # Prepare a results dictionary
    results = {}

    # Assert that the pattern matches the leaf and the results are updated with the name
    assert pattern.match(mock_leaf, results)
    assert "mock_name" in results and results["mock_name"] is mock_leaf

# Run the tests
pytest.main()
